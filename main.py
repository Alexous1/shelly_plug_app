# import libraries
import urllib
from flask import Flask
import json
from tkinter import *

app = Flask(__name__)

# create the window to control the  app
trr = Tk()
trr.geometry("300x300")
trr.config(background='#41B77F')

# make the function to turn off the shelly plug

def off():
    urlData = "http://192.168.1.27/relay/0?turn=off"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    json.loads(data.decode(encoding))
    trr.quit()

# make the function to turn on the shelly plug
def on():
    urlData = "http://192.168.1.27/relay/0?turn=on"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    a = json.loads(data.decode(encoding))
    trr.quit()


# make the button to turn on the shelly plug
button = Button(trr, text='allumer', command=on)
button.pack(expand=YES)

# make the button to turn off the shelly plug
button1 = Button(trr, text='eteindre', command=off)
button1.pack(expand=YES)

# main loop
trr.mainloop()