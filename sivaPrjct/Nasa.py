import requests
import os
from PIL import Image
import pyttsx3


engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

Api_Key = "7Ba5WPOGccPZTueFo6EDRgk4AceVDHKhj2LBZePF"

def NasaNews(Date):
    Speak("Extracting Data From Nasa . ")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_Key)
    Params = {'date': str(Date)}
    r = requests.get(Url, params=Params)
    Data = r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    FileName = str(Date) + '.jpg'
    with open(FileName, 'wb') as f:
        f.write(Image_r.content)
    Path_1 = "//Users//harshsoni//Documents//sivaPrjct//" + str(FileName)
    Path_2 = "//Users//harshsoni//Documents//sivaPrjct//DataBase//NasaImg//" + str(FileName)
    os.rename(Path_1, Path_2)
    img = Image.open(Path_2)
    img.show()
    Speak(f"Title : {Title}")
    Speak(f"According To Nasa : {Info}")

