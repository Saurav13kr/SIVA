import webbrowser as web
import pywhatkit
import pyttsx3
import wikipedia
import os , sys , subprocess
import requests
import bs4

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def Youtubesearch(search):
    result = "https://www.youtube.com/results?search_query="+search
    web.open(result)
    Speak("this is what i found ")
    pywhatkit.playonyt(search)

def Wikipedia(query):
    Speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    Speak("According to Wikipedia")
    print(results)
    Speak(results)


def CoronaVirus(Country):
    countries = str(Country).replace(" ", "")
    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"
    result = requests.get(url)
    soups = bs4.BeautifulSoup(result.text, 'lxml')
    corona = soups.find_all('div', class_='maincounter-number')
    Data = []
    for case in corona:
        span = case.find('span')
        Data.append(span.string)
    cases, Death, recovored = Data
    Speak(f"Cases : {cases}")
    Speak(f"Deaths : {Death}")
    Speak(f"Recovered : {recovored}")




