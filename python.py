import subprocess
from urllib import request
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import twilio
import winshell
import smtplib
import time
import googletrans 


engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
recognizer=sr.Recognizer()

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
        speak('I am your voice assistant JO.....')
        speak('How can i Help you at the moment ?')
  
    elif hour>= 12 and hour<15:
        speak("Good Afternoon Sir !")
        speak('I am your voice assistant JO.....')
        speak('How can i Help you at the moment ?')
  
    else:
        speak("Good Evening Sir !")
        speak('I am your voice assistant JO......')
        speak('How can i help you at the moment ?')


def new_func():
    return 5




def takeCommand():
     
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        r.pause_threshold =  0.5
    try:
        query = r.recognize_google(audio).lower()
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! TRY Writing your command Sir')
        query = str(input('Command: '))

    return query
     
    

if __name__ == '__main__':

        clear = lambda: os.system('cls')
        clear()
        greetMe()
        takeCommand()

        while True:

            query = takeCommand().lower()

            if 'wikipededia' in query:
                speak('searching wikipedia.......')
                query = query.replace("wikipedia"," ")
                results = wikipedia.summary( query, sentances = 3)
                speak('According to wikipedia')
                print(results)
                speak(results)

            elif 'youtube' in query:
                b='opening youtube'
                engine.say(b)
                engine.runAndWait()
                webbrowser.open('www.youtube.com')

            elif 'open google traslate' in query:
                b='opening google translate sir'
                engine.say(b)
                engine.runAndWait()
                webbrowser.open('https://translate.google.co.in')

            elif 'open blog' in query:
                b='opening your blogger'
                engine.say(b)
                engine.runAndWait()
                webbrowser.open('https://www.blogger.com/blog/posts/9102196285998194533?tab=rj')

            elif 'edge'in query:
                a='Opening edge..'
                engine.say(a)
                engine.runAndWait()
                programName = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
                subprocess.Popen([programName])

                
            elif 'how are you' in query :
                stMsgs = ('I am nice and full of energy sir..')
                speak(stMsgs)
                speak("How are you sir!..")
                print(stMsgs)

            elif 'whatsapp' in query:
                b='opening whatsapp'
                engine.say(b)
                engine.runAndWait()
                webbrowser.open_new_tab('https://web.whatsapp.com/')

            elif "restart" in query:
                speak("Make sure all the application are closed before restart")
                os.system("shutdown /r /t 1")

            elif 'write a note' in query:
                speak("What shuld i write, sir")
                note = takeCommand()
                file = open('doc.txt', 'w')
                speak("sir , should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.new().strftime(" %H: %M: %S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif 'what is the time'in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
            
            elif 'open bing' in query:
                b='opening bing search engine'
                engine.say(b)
                engine.runAndWait()
                webbrowser.open_new_tab('www.bing.com')

            elif ' meet' in query:
                b='opening Google meet'
                engine.say(b)
                engine.runAndWait()
                webbrowser.open_new_tab('https://meet.google.com/')


                if "wikipedia" in query:
                    webbrowser.open_new_tab("www.wikipedia.com")