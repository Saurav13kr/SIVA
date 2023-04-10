from tkinter import *
from tkinter import Button
from main import TaskExe
def main_screen():
    global screen
    screen = Tk()
    screen.title("S.I.V.A")
    screen.geometry("100x250")
    screen.iconbitmap('app_icon.ico')

    name_label = Label(text = "S.I.V.A" ,width = 300, bg = "black", fg="white", font = ("Calibri", 13))
    name_label.pack()
    microphone_photo = PhotoImage(file ="Jarvis_Gui(1).gif")
    microphone_button = Button(image=microphone_photo, command = TaskExe)
    microphone_button.pack(pady=10)
    screen.mainloop()

main_screen()