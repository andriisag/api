import requests
import json
import tkinter as tk
import webbrowser


def search():
        a = entry.get()
        url = "https://free-news.p.rapidapi.com/v1/search"

        querystring = {"q": f"{a}","lang":"en"}

        headers = {
	          "X-RapidAPI-Key": "ca96ed25a2mshdefe4a6da7eed38p1fd92fjsne956cd89feb5",
	          "X-RapidAPI-Host": "free-news.p.rapidapi.com"
               }
        response = requests.request("GET", url, headers=headers, params=querystring)

        jsonv = response.json()

        label1.config(text = jsonv['articles'][0]['title'])
        label2.config(text = jsonv['articles'][0]['link'])
        


def callback(event):
        a = entry.get()
        url = "https://free-news.p.rapidapi.com/v1/search"

        querystring = {"q": f"{a}","lang":"en"}

        headers = {
	          "X-RapidAPI-Key": "ca96ed25a2mshdefe4a6da7eed38p1fd92fjsne956cd89feb5",
	          "X-RapidAPI-Host": "free-news.p.rapidapi.com"
               }
        response = requests.request("GET", url, headers=headers, params=querystring)

        jsonv = response.json()

        webbrowser.open_new(jsonv['articles'][0]['link'])



window = tk.Tk()
window.minsize(500, 200)

entry = tk.Entry()
button = tk.Button(
    text="search",
    width=20,
    height=5,
    command=search
    )
label1 = tk.Label()
label2 = tk.Label() 

entry.pack()
button.pack()
label1.pack()
label2.pack()
label2.bind("<Button-1>", callback)

window.mainloop()
