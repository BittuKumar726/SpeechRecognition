import pyttsx3
import speech_recognition as sr
import sys
import re
import smtplib
import requests
import subprocess
import datetime
import wikipedia
import webbrowser
import urllib
import os
import json
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import wikipedia
import random
from time import strftime
import urllib.request #used to make requests
import urllib.parse #used to parse values into the url
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xml.etree.ElementTree as ET
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    import datetime
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am Mahi sir, Please tell me how may iI help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')

        print(f"User said :{query}\n")
        
    except Exception as e:
        speak("Say that again please...")
        print("Say that again please...")
        query = takeCommand();
    return query

if __name__ == "__main__":
    wishMe()

    while 1:
    #if 1:  
        query = takeCommand().lower() 
        if 'can you hear me' in query:
            speak('Yes sir. How can I help you Sir!')

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia"," ")

            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            speak("Or any thing Sir!!")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        #elif 'open google' in query:
            #webbrowser.open("google.com")

        elif 'play music' in query:
            speak("Ok Sir!!")
            music_dir = 'F:\\Music\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            speak("MUSIC now playing Sir!!. Enjoy it SIR!. Or anything Sir!")
        elif 'open gaana' in query:
            webbrowser.open("gaana.com")
            speak("your gaana app now open sir!. Enjao it Sir!")
        elif 'time' in query:
            import datetime
            now = datetime.datetime.now()
            speak('Current time is %d hours %d minutes' %(now.hour, now.minute))
            speak("Or any thing Sir!!")
        elif 'news' in query:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page = soup(xml_page, "html")
                  #soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:15]:
                    print(news.title.get_text())
                    #print(news.link.get_text())
                    #print(news.pubDate)
                    print("-"*100)
                    speak(news.title.get_text())
                speak("Or- anythings Sir!")
            except Exception as e:
                  print(e)

        elif 'launch' in query:
            speak("okay!")
            reg_ex = re.search('launch (.*)',query)
            if reg_ex:
                appname = reg_ex.group(1)
                appname1 = appname+".exe"
                subprocess.Popen(appname1)
                #subprocess.Popen([r'C:\Program Files\Microsoft Office\Office12\MSACCESS.EXE',r'\\vopcc\gis\GISOPS\StreetNetwork\Routing.mdb'])
                subprocess.Popen(["open", "-n", "/C:/Program Files (x86)/" + appname1], stdout=subprocess.PIPE)
                subprocess.Popen(["open", "-n", "/Application/" + appname1], stdout=subprocess.PIPE)
            speak('I have launched the desired application')
            
        elif 'youtube' in query:
            speak('Ok!')
            reg_ex = re.search('youtube (.+)', query)
            if reg_ex:
                domain = query.split("youtube",1)[1] 
                query_string = urllib.parse.urlencode({"search_query" : domain})
                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string) 
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode()) # finds all links in search result
                webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
                pass         
            speak('your desired video is now opened Sir!.Enjoy it. or anything else sir!')
        elif 'open google and search' in query:
            reg_ex = re.search('open google and search (.*)', query)
            search_for = query.split("search",1)[1]
            url = 'https://www.google.com/'
            if reg_ex:
                subgoogle = reg_ex.group(1)
                url = url + 'r/' + subgoogle
                speak('Okay!')
                driver = webdriver.Firefox(executable_path='C:/Users/Asus/AppData/Local/Programs/Python/geckodriver') #depends which web browser you are using
                driver.get('http://www.google.com')
                search = driver.find_element_by_name('q') # finds search
                search.send_keys(str(search_for)) #sends search keys 
                search.send_keys(Keys.RETURN) #hits enter
            speak('your  query  is  now  searching  Sir! . or  anything  else  sir!')
        elif 'thank you' in query:
            speak("Most welcome sir!!!. and anythings sir")
        elif 'no' in query:
            speak("Bye bye sir. Have a nice day")
            sys.exit()