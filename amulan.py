import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import requests
import webbrowser as web
import os
import mechanicalsoup
import beepy


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


def speech_to_text():
    # try:
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
            
        except sr.UnknownValueError:
            pass
            #print("Oops! Didn't catch that")
        except sr.RequestError as e:
            speakthis("Ohh my God! Cannot connect from Google API; {0}".format(e))
            pass
    
    # except KeyboardInterrupt:
    #      pass
        return command

def RunBot():
    command = speech_to_text()
    if command == '':
        pass
    elif 'alexa' == command:        
        speakthis("Yes? what can I do for you")
        beepy.make_sound.beep(sound=3)
        command = speech_to_text()
        features(command)
    elif 'alexa' in command:
        command = command.lower()
        command = command.replace('alexa ','')
        features(command)
 
def features(command):
    if 'play' in command:
        song = command.replace('play ', '')
        speakthis('playing ' + song)
        kit.playonyt(song)
    elif 'search' in command:
        search = command.replace('search ', '')
        speakthis('searching ' + search)
        kit.search(search)
    elif 'what is' in command:
        fetch = command.replace('what is ', '')
        speakthis('Based on internet what is' + fetch)
        speakthis(kit.info(fetch,3,1))
    elif 'who is' in command:
        fetch = command.replace('who is ', '')
        speakthis('Based on internet who is' + fetch)
        speakthis(kit.info(fetch,3,1))
    elif 'define' in command:
        fetch = command.replace('define ', '')
        speakthis('Based on internet define' + fetch)
        speakthis(kit.info(fetch,3,1))
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speakthis('the time is ' + time)
    elif 'code blue' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speakthis('the time is ' + time)
        os.system('nmcli c up Integritynet')
        browser = mechanicalsoup.StatefulBrowser()
        browser.open('http://192.168.149.54:5959/login#no-back-button')
        browser.select_form('form[method="POST"]')
        browser["username"] = "009819"
        browser["password"] = "pass1"
        browser.submit_selected()
        if 'http://192.168.149.54:5959/#no-back-button' == browser.get_url():
            speakthis("You have successfully timed in")
        else:
            speakthis("Somethings wrong")
        browser.close()
        #print(browser.get_url())
    elif 'code red' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speakthis('the time is ' + time)
        os.system('nmcli c up Integritynet')
        web.open("http://192.168.149.54:5959/#no-back-button")
    else:
        speakthis('Sorry try again')
        
    # def search(topic: str) -> None:
    # """Searches about the topic on Google"""
    # link = 'https://www.google.com/search?q={}'.format(topic)
    # web.open(link)

while True:
    RunBot()
