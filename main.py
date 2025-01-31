# import section
import webbrowser
import pyttsx3
import os
import speech_recognition as sr
import requests
import datetime
from bs4 import BeautifulSoup
import pyautogui
import random
import speedtest
# import section end
# =======================================
# voice rate and voice model
engine = pyttsx3.init()
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
# voice section end

# =======================================
# Speak section
def speak(command):
    engine.say(command)
    engine.runAndWait()

# Speak section end
# =======================================
# Mic section
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("You didn't say anything")
        return "None"
    return query


def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

# =======================================
# Main execution
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, you can call me anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "the time" in query:
                 strTime = datetime.datetime.now().strftime("%H:%M")    
                 speak(f"Sir, the time is {strTime}")
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                 from Dictapp import closeappweb
                 closeappweb(query)
                elif "temperature" in query:
                    search = "temperature in Dhaka"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in Dhaka"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "the time" in query:
                   strTime = datetime.datetime.now().strftime("%H:%M")    
                   speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                  speak("Going to sleep,sir")
                  exit()
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                     from Dictapp import closeappweb
                     closeappweb(query)
                elif "set an alarm" in query:
                   print("input time example:- 10 and 10 and 10")
                   speak("Set the time")
                   a = input("Please tell the time :- ")
                   alarm(a)
                   speak("Done,sir")
                elif "pause" in query:
                  pyautogui.press("k")
                  speak("video paused")
                elif "play" in query:
                  pyautogui.press("k")
                  speak("video played")
                elif "mute" in query:
                  pyautogui.press("m")
                  speak("video muted")
                elif "volume up" in query:
                 from keyboard import volumeup
                 speak("Turning volume up,sir")
                 volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                elif "remember that" in query:
                 rememberMessage = query.replace("remember that","")
                 rememberMessage = query.replace("jarvis","")
                 speak("You told me to remember that"+rememberMessage)
                 remember = open("Remember.txt","a")
                 remember.write(rememberMessage)
                 remember.close()
                elif "what do you remember" in query:
                 remember = open("Remember.txt","r")
                 speak("You told me to remember that" + remember.read())
                elif "tired" in query:
                 speak("Playing your favourite songs, sir")
                 a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                 b = random.choice(a)
                 if b==1:
                  webbrowser.open("https://www.youtube.com/watch?v=2i2khp_npdE&list=RDQM1gzxREez0Ig&start_radio=1")
                elif "news" in query:
                 from NewsRead import latestnews
                 latestnews()
                elif "calculate" in query:
                 from Calculatenumbers import WolfRamAlpha
                 from Calculatenumbers import Calc
                 query = query.replace("calculate","")
                 query = query.replace("jarvis","")
                 Calc(query)
                elif "whatsapp" in query:
                 from Whatsapp import sendMessage
                 sendMessage()
                elif "shutdown the system" in query:
                 speak("Are You sure you want to shutdown")
                 shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                 if shutdown == "yes":
                  os.system("shutdown /s /t 1")

                elif shutdown == "no":
                      break
                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")  
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)