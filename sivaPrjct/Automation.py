import subprocess
import os
import webbrowser as web
from keyboard import press_and_release
from pyautogui import hotkey
from pyautogui import click
from keyboard import press
from keyboard import write
import pyttsx3
import speech_recognition as sr
from time import sleep
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


def WhatsappMsg(name, message):
    sleep(5)
    click(x=442, y=866)
    sleep(10)
    click(x=209, y=81)
    sleep(1)
    write(name)
    sleep(0.5)
    click(x=132, y=214)
    sleep(0.5)
    click(x=651, y=859)
    sleep(0.5)
    write(message)
    press('enter')

def WhatsappCall(name):
    sleep(5)
    click(x=442, y=866)
    sleep(10)
    click(x=209, y=81)
    sleep(1)
    write(name)
    sleep(1)
    click(x=132, y=214)
    sleep(1)
    click(x=1290, y=36)

def OnlinClass(Subject):
    Speak("Joining The Class Sir .")
    if 'dbms' in Subject:
        web.open("https://meet.google.com/npk-dewi-yuz")
        sleep(5)
        keyboard.press(Key.cmd)
        keyboard.press('d')
        keyboard.release(Key.cmd)
        keyboard.release('d')
        keyboard.press(Key.cmd)
        keyboard.press('e')
        keyboard.release(Key.cmd)
        keyboard.release('e')
        sleep(4)
        click(x=1037, y=512)
        sleep(1)
def wtr():
    Speak("what do you want to write")
    cwr = TakeCommand()
    write(cwr)

def mwtr():
    wtr()
    Speak("shoud we continue")
    kk = TakeCommand()
    if 'continue' in kk:
        mwtr()
    elif 'save' in kk:
        keyboard.press(Key.cmd)
        keyboard.press('s')
        keyboard.release(Key.cmd)
        keyboard.release('s')
        keyboard.press(Key.delete)
        keyboard.release(Key.delete)
        Speak("What should be the title of the file")
        rr=TakeCommand()
        write(rr)
        click(x=984, y=636)
    else:
        return

def Msword():
    sleep(4)
    click(x=805, y=854)
    sleep(2)
    keyboard.press(Key.cmd)
    keyboard.press('n')
    keyboard.release(Key.cmd)
    keyboard.release('n')
    mwtr()
def ivtfrorm():
    web.open("https://docs.google.com/forms/d/16L52qHv29_5UVleP0TLUgFu2io-HBGPqOjbhGcyuADc/edit")
    sleep(5)
    click(x=470, y=548)
    Speak("Discriptiion")
    wtr()
    Speak("Form created")
    keyboard.press(Key.cmd)
    keyboard.press(Key.enter)
    keyboard.release(Key.cmd)
    keyboard.release(Key.enter)
    sleep(2)
    click(x=645, y=288)
    sleep(1)
    click(x=965, y=443)







