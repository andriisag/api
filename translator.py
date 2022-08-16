import requests
from tkinter import *
from tkinter import StringVar
from tkinter import OptionMenu


root = Tk()
root.geometry( "200x200" )


options = [
    "en",
    "de",
    "es"
]
options2 = [
     "en",
    "de",
    "es"
]

variable = StringVar()
variable2 = StringVar()
variable.set("en")
variable2.set("en")
drop = OptionMenu( root , variable, *options )
drop2 = OptionMenu( root , variable2 , *options2 )
entry = Entry()
label = Label()

def api():
	text1 = entry.get()
	menu1 = variable.get()
	menu2 = variable2.get()


	url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

	payload =  {
    "q": f"{text1}",
    "source": f"{menu1}",
    "target": f"{menu2}"
    }
	headers = {
	"content-type": "application/json",
    "X-RapidAPI-Key": "f0eda7c17amsha10f3c793fdf668p1ba57fjsn4b46df9be184",
    "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
    }
	response = requests.request("POST", url, json=payload, headers=headers)
	label.config( text = response.text["data"])

button = Button(
    text="Перекласти",
    width=20,
    height=5,
    command=api
    )
    
entry.pack()
drop.pack()
label.pack()
drop2.pack()
button.pack()

root.mainloop()
