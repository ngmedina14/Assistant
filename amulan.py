import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime

r = sr.Recognizer()
m = sr.Microphone()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)
engine.setProperty('rate', 150)
engine.setProperty('volume',1.0)

#The machine will speak anything that you put inside this function
def speakthis(text):
    engine.say(text)
    print(text)
    engine.runAndWait()


def take_command():
        try:
            with m as source: r.adjust_for_ambient_noise(source)
            print("Listening")
            with m as source: audio = r.listen(source)
            print("Processing...")
            try:
                # recognize speech using Google Speech Recognition
                command = ''
                command = r.recognize_google(audio)

                # we need some special handling here to correctly print unicode characters to standard output
                if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                    command = u"{}".format(command).encode("utf-8")
                else:  # this version of Python uses unicode for strings (Python 3+)
                    command = "{}".format(command)
                if 'alexa' in command:
                    command = command.lower()
                    command = command.replace('alexa ','')
                    return command
            except sr.UnknownValueError:
                pass
                #print("Oops! Didn't catch that")
            except sr.RequestError as e:
                speakthis("Ohh my God! Cannot connect from Google API; {0}".format(e))
                pass
        
        except KeyboardInterrupt:
            pass
        command = ''
        return command

def RunBot():
    command = take_command()
    print(command)
    #   search pywhatkit.search
    #   what is pywhatkit.info
    if 'play' in command:
        song = command.replace('play ', '')
        speakthis('playing ' + song)
        kit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speakthis('the time is ' + time)
    # elif 'who the heck is' in command:
    #     person = command.replace('who the heck is', '')
    #     info = wikipedia.summary(person, 1)
    #     print(info)
    #     talk(info)
    # elif 'date' in command:
    #     talk('sorry, I have a headache')
    # elif 'are you single' in command:
    #     talk('I am in a relationship with wifi')
    # elif 'joke' in command:
    #     talk(pyjokes.get_joke())


while True:
    RunBot()
