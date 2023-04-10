import os
import pyautogui
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import pyttsx3
import speech_recognition as sr
from time import sleep
import webbrowser as web
from pynput.keyboard import Key, Controller
keyboard = Controller()


engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)


def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source)
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(": Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f": Your Command : {query}\n")
    except:
        return ""
    return query.lower()
# TakeCommand()
def TaskExe():
    run = 1
    while run==1:
        query = TakeCommand() 
        print(query)
        run += 1
        if 'youtube search' in query:
            Query = query.replace("Shiva", "")
            query = Query.replace("YouTube search", "")
            from Feature import Youtubesearch
            Youtubesearch(query)
        elif 'wikipedia' in query:
            from Feature import Wikipedia
            Wikipedia(query)
        elif 'whatsapp message' in query:
            name = query.replace("whatsapp message", "")
            name = name.replace("send ", "")
            name = name.replace("to ", "")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automation import WhatsappMsg
            WhatsappMsg(Name, MSG)
        elif 'call' in query:
            from Automation import WhatsappCall
            name = query.replace("call ", "")
            name = name.replace("shiva ", "")
            Name = str(name)
            WhatsappCall(Name)
        elif 'chrome new tab' in query:
            sleep(5)
            keyboard.press(Key.cmd)
            keyboard.press('t')
            keyboard.release(Key.cmd)
            keyboard.release('t')
        elif 'chrome close tab' in query:
            sleep(5)
            keyboard.press(Key.cmd)
            keyboard.press('w')
            keyboard.release(Key.cmd)
            keyboard.release('w')
        elif 'chrome new window' in query:
            sleep(5)
            keyboard.press(Key.cmd)
            keyboard.press('n')
            keyboard.release(Key.cmd)
            keyboard.release('n')
        elif 'chrome history' in query:
            sleep(5)
            keyboard.press(Key.cmd)
            keyboard.press('h')
            keyboard.release(Key.cmd)
            keyboard.release('h')
        elif 'chrome download' in query:
            sleep(5)
            keyboard.press(Key.cmd)
            keyboard.press('j')
            keyboard.release(Key.cmd)
            keyboard.release('j')
        elif 'chrome bookmark' in query:
            sleep(5)
            keyboard.press(Key.cmd)
            keyboard.press('d')
            keyboard.release(Key.cmd)
            keyboard.release('d')
            press('enter')
        elif 'chrome incognito' in query:
            sleep(5)
            keyboard.press(Key.cmd)
            keyboard.press(Key.shift)
            keyboard.press('n')
            keyboard.release(Key.cmd)
            keyboard.release(Key.shift)
            keyboard.release('n')
        elif 'chrome switch tab' in query:
            sleep(5)
            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to", "")
            num = Tab
            bb = f'cmd + {num}'
            press_and_release(bb)
            keyboard.press(bb)
            keyboard.release(bb)
        elif 'chrome open' in query:
            sleep(5)
            name = query.replace("open ", "")
            NameA = str(name)
            if 'youtube' in NameA:
                web.open("https://www.youtube.com/")
            elif 'instagram' in NameA:
                web.open("https://www.instagram.com/")
            else:
                string = "https://www." + NameA + ".com"
                string_2 = string.replace(" ", "")
                web.open(string_2)
        elif 'pause' in query:
            press('space bar')
        elif 'resume' in query:
            press('space bar')
        elif 'full screen' in query:
            press('f')
        elif 'film screen' in query:
            press('t')
        elif 'skip' in query:
            press('l')
        elif 'back' in query:
            press('j')
        elif 'increase' in query:
            keyboard.press(Key.shift)
            keyboard.press('.')
            keyboard.release(Key.shift)
            keyboard.release('.')
        elif 'decrease' in query:
            keyboard.press(Key.shift)
            keyboard.press(',')
            keyboard.release(Key.shift)
            keyboard.release(',')
        elif 'previous' in query:
            keyboard.press(Key.shift)
            keyboard.press('p')
            keyboard.release(Key.shift)
            keyboard.release('p')
        elif 'next' in query:
            keyboard.press(Key.shift)
            keyboard.press('n')
            keyboard.release(Key.shift)
            keyboard.release('n')
        elif 'mute' in query:
            press('m')
        elif 'unmute' in query:
            press('m')

        elif 'nasa' in query:
            Speak(f"Whats The Date")
            dt=TakeCommand()
            dt=dt.replace(" and ","-")
            from Nasa import NasaNews
            NasaNews(dt)
        elif 'open whiteboard' in query:
            web.open("https://www.tutorialspoint.com/whiteboard.htm")
        elif 'draw a square' in query:
            sleep(5)
            pyautogui.click(608,390)
            pyautogui.dragTo(812, 390, duration=0.2, button='left')
            pyautogui.dragTo(812, 594, duration=0.2, button='left')
            pyautogui.dragTo(608, 595, duration=0.2, button='left')
            pyautogui.dragTo(608,390, duration=0.2, button='left')
        elif 'draw a triangle' in query:
            sleep(5)
            pyautogui.click(727,411)
            pyautogui.dragTo(809,574, duration=0.2, button='left')
            pyautogui.dragTo(641, 574, duration=0.2, button='left')
            pyautogui.dragTo(727,411, duration=0.2, button='left')
        elif 'draw a horizontal line' in query:
            sleep(5)
            pyautogui.click(369, 495)
            pyautogui.dragTo(1206,495, duration=0.2, button='left')
        elif 'draw a vertical line' in query:
            sleep(5)
            pyautogui.click(673, 205)
            pyautogui.dragTo(673,792, duration=0.2, button='left')
        elif 'online' in query:
            from Automation import OnlinClass
            Speak("Tell Me The Name Of The Class .")
            Class = TakeCommand()
            OnlinClass(Class)
        elif 'ms word' in query:
            from Automation import Msword
            Msword()
        elif 'covid cases' in query:
            from Feature import CoronaVirus
            Speak("Which Country's Information ?")
            cccc = TakeCommand()
            CoronaVirus(cccc)
TaskExe()
