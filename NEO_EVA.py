import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests
import sys
#colors
import colored
import sys
from colored import fg, bg, attr
from colored import stylize

#voice
engine=pyttsx3.init() 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #male 0 famale 1
rate = engine.getProperty('rate') 
engine.setProperty('rate', 175)
clear = lambda: os.system('cls')
EVAsleep = bool(False)

def password():

    UserName = input ("Enter Username: ")
    PassWord = input ("Enter Password: ")

    if UserName == 'Aon' and PassWord == '123':
        time.sleep(1)
        print ("Login successful!")
        logged()

    else:
        print ("Password did not match!")
        time.sleep(1)
        sys.exit()

def logged():
    time.sleep(2)
    print ("Welcome to NEO EVA")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=3 and hour<12:
        speak("Good Morning")
        cprint("EVA: Good Morning\n",222,0,0)
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        cprint("EVA: Good Afternoon\n",214,0,0)
    else:
        speak("Good Evening")
        cprint("EVA: Good Evening\n",19,0,0)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        cprint("Listening...", 240,0,0)
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak('No recognition')
            return "None"
        return statement

def EVAwake():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            #print(f"user said:{statement}\n")

        except Exception as e:
            return "None"
        return statement

def cprint(text,f,b,s):
    color = bg(b) + fg(f)
    style = attr(s)
    reset = attr('reset')
    print(color + text + style + reset)

def internetCheck():
    try:
        request = requests.get("http://www.google.com", timeout=5)
        cprint("Internet Connection = ON\n",2 ,0 , 0)
        speak("Connected to Internet")
    except (requests.ConnectionError, requests.Timeout) as exception:
        cprint("Internet Connection = OFF\n",1 ,0 , 0)
        speak("No internet connection")   

def Ascii():
    cprint(' b.             8 8 888888888888     ,o888888o.                8 888888888888 `8.`888b           ,8` .8.', 129 ,0,0)
    cprint(' 888o.          8 8 8888          . 8888     `88.              8 8888          `8.`888b         ,8` .888.', 129 ,0,0)
    cprint(' Y88888o.       8 8 8888         ,8 8888       `8b             8 8888           `8.`888b       ,8` :88888.', 128 ,0,0)
    cprint(' .`Y888888o.    8 8 8888         88 8888        `8b            8 8888            `8.`888b     ,8` . `88888.', 128 ,0,0)
    cprint(' 8o. `Y888888o. 8 8 888888888888 88 8888         88            8 888888888888     `8.`888b   ,8` .8. `88888.', 127 ,0,0)
    cprint(' 8`Y8o. `Y88888o8 8 8888         88 8888         88            8 8888              `8.`888b ,8` .8`8. `88888.', 127 ,0,0)
    cprint(' 8   `Y8o. `Y8888 8 8888         88 8888        ,8P            8 8888               `8.`888b8` .8` `8. `88888.', 126 ,0,0)
    cprint(' 8      `Y8o. `Y8 8 8888         `8 8888       ,8P             8 8888                `8.`888` .8`   `8. `88888.', 126 ,0,0)
    cprint(' 8         `Y8o.` 8 8888          ` 8888     ,88               8 8888                 `8.`8` .888888888. `88888.', 125 ,0,0)
    cprint(' 8            `Yo 8 888888888888     `8888888P`                8 888888888888          `8.` .8`       `8. `88888.', 125 ,0,0)
    print('\n')

#password()
clear()

Ascii()

cprint('Loading your AI personal assistant Neo EVA', '125', '0' , 'bold')
speak("Loading your AI personal assistant Neo EVA")

internetCheck()

wishMe()

if __name__=='__main__':
    while True:
        if EVAsleep is True:
            EvaState = EVAwake().lower()
            if EvaState ==0:
                continue
            else:
                if "wake up" in EvaState:
                    speak('Waking up')
                    EVAsleep = False
                    time.sleep(1)
        else:
            speak("Can I help you?")
            statement = takeCommand().lower()
            if statement==0:
                continue

            elif "sleep mode" in statement:
                speak('Sleep mode activate')
                EVAsleep = True
                time.sleep(1)

            elif "close application" in statement:
                speak('Closing application. Good bye')
                print('Good bye')
                break

            elif 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'search'  in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(2)    

            elif 'youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(2)

            elif 'google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(2)

            elif 'gmail' in statement:
                webbrowser.open_new_tab("https://gmail.com")
                speak("Google Mail open now")
                time.sleep(2)

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")
            
            elif 'who are you' in statement:
                speak('I am Neon EVAH version 1 point O your personal assistant. I am programmed to minor tasks like'
                      'opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia and more')

            elif "who made you" in statement or "who created you" in statement:
                speak("I was built by Louis")
                print("I was built by Louis")

            elif 'close application' in statement:
                sys.exit()   
                time.sleep(5) 

            elif "shut down" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                os.system('shutdown -s')

