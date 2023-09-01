# import libraries
import urllib
from flask import Flask
import json
from tkinter import *
import customtkinter

app = Flask(__name__)

# create the window to control the Shelly Plug

# define the appearance mode
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# create the window
root = customtkinter.CTk()
root.geometry("200x140")


# make the function to turn on the Shelly Plug
def on():
    urlData = "http://192.168.1.27/relay/0?turn=on"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    a = json.loads(data.decode(encoding))
    root.quit()

# make the function to turn off the Shelly Plug
def off():
    urlData = "http://192.168.1.27/relay/0?turn=off"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    json.loads(data.decode(encoding))
    root.quit()

# Create a label to explain the buttons
explain = customtkinter.CTkLabel(root, text="Control you Shelly Plug")
explain.pack(expand=YES)

# make the button to turn on the Shelly Plug
OnButton = customtkinter.CTkButton(root, text='on', command=on)
OnButton.pack(expand=YES)

# make the button to turn off the Shelly Plug
OffButton = customtkinter.CTkButton(root, text='off', command=off)
OffButton.pack(expand=YES)

# main loop
root.mainloop()