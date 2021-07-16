import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import urllib
import random
import Crypt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I'm Jarvis Ma'am. Please tell me how could I help you")

def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognising....")
        query = r.recognize_google(audio, language = 'en-US')
        print("user said\n", query)
        
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('anakshi99@gmail.com', 'password')
    #server.sendmail('anakshi99@gmail.com', to, content)
    #server.close()
    Crypt.Login(to, content)

if __name__ in "__main__":
    speak("Hello Ma'am")
    wishMe()
    while True:
        query = takeCommand().lower()
    
    # logic for executing tasks
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            querry = querry.replace("wikipedia","")
            results = wikipedia.summary(querry,sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'play music' in query:
            music_dir = 'c:\\Users\\Dell\\Desktop\\Python 3.9\\audio'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Ma'am, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to soma' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "dsoma8307@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend! I am not able to send this email")    
        
        elif 'that will be all' in query or 'bye' in query or 'close' in query:
            speak("Have a Nice Day Ma'am!")
            sys.exit()


