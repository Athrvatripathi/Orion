import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import pyautogui as pyag
import time as t

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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

    speak("I am Orion, Atharv Tripathi's Personal Assistant")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            wb.open("youtube.com")

        elif 'open google' in query:
            wb.open("google.com")

        elif 'open stackoverflow' in query:
            wb.open("stackoverflow.com")   


        elif 'play music' in query:
            wb.open("https://www.youtube.com/watch?v=o4aumjnQJYo")
        

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Apoorva Tripathi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'write a mail' in query:
            wb.open("gmail.com")   #Most of us use gmail. So, I've written the code compatible to gmail. You can change it as per your preferred mail service provider. 
        
        elif 'open whatsApp' in query:
            wb.open("web.whatsapp.com")

        elif 'open spotify' in query:
            wb.open("open.spotify.com")

        elif 'open snapchat' in query:
            wb.open("web.snapchat.com")  

        elif 'quit' in query:
            exit()  

        elif 'go away' in query:
            engine.say("cool")
            exit()  

        elif 'get lost' in query:
            engine.say("Cool, bye") 
            exit()

        elif 'bye' in query:
            engine.say("bye")
            exit()


