import pyttsx3
import datetime
import speech_recognition as sr 

engine = pyttsx3.init()
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)

def speak(command):
    engine.say(command)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning, Sir")
    elif hour>12 and  hour<=18:
        speak("Good Afternoon, Sir")
    else:
        speak("Good Evening, Sir")

    speak("Please tell me, How can I help you ?")
    