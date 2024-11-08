import requests
import json
import os
os.system('clear')
from time import sleep, strftime, gmtime
import tkinter as tk
import random
import customtkinter
import tkintermapview
import sqlite3
import datetime


try:
    
    window = customtkinter.CTk()
    window.geometry("1000x650")
    window.title("Időjárás")
    window.resizable(0, 0)
    label = customtkinter.CTkLabel(window, text="Írj be egy települést vagy országot", font=("Helvetica", 24))
    #lat = 47.49
    #lon = 19.34
    api = "a3c3ac028697416ece9bd3c3a7c0f500"
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    """def remover():
        pass"""
    def lightd():
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("light")
        text_entry = customtkinter.CTkEntry(master=window,
                                    placeholder_text="Település / Ország",
                                    width=200,
                                    height=20,
                                    font=("Helvetica", 18),
                                    corner_radius=50,
                                    text_color="green",
                                    placeholder_text_color="lightblue",
                                    fg_color=("blue", "darkblue"),
                                    state="normal")

    def dark():
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

    def history():
        gtime = ""
        con = sqlite3.connect("weather.db")
        cur = con.cursor()
        cur.execute("SELECT time FROM weather;")
        times = cur.fetchall()
        for time in times:
            print(f"Mentett idők: {time}")
        #print(times)
        cur.execute("SELECT * FROM weather;")
        citys = cur.fetchone()
        print(citys)
        
        print(f"\n{gtime}")

    """light = customtkinter.CTkButton(master=window,
                                    width=120,
                                    height=32,
                                    border_width=0,
                                    corner_radius=10,
                                    text="Világos",
                                    hover_color="lightblue",
                                    command=lightd)

    light.place(relx=0.01, rely=0)"""

    dark = customtkinter.CTkButton(master=window,
                                    width=120,
                                    height=32,
                                    border_width=0,
                                    corner_radius=10,
                                    text="Sötét",
                                    hover_color="lightblue",
                                    command=dark)

    dark.place(relx=0.14, rely=0)
    history = customtkinter.CTkButton(master=window,
                                    width=120,
                                    height=32,
                                    border_width=0,
                                    corner_radius=10,
                                    text="Lementett előzmények",
                                    hover_color="lightblue",
                                    command=history)

    history.place(relx=0.1, rely=0)
    text_entry = customtkinter.CTkEntry(master=window,
                                    placeholder_text="Település / Ország",
                                    width=200,
                                    height=20,
                                    font=("Helvetica", 18),
                                    corner_radius=50,
                                    text_color="green",
                                    placeholder_text_color="darkblue",
                                    fg_color=("blue", "lightblue"),
                                    state="normal")


    def submit_input():
        varos = text_entry.get()
        lekerdez = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={varos}&appid=a3c3ac028697416ece9bd3c3a7c0f500&units=metric')
        jsonformatum = json.loads(lekerdez.text)
        message = customtkinter.CTkLabel(window, text=f"Város: {jsonformatum['name']}", font=("Helvetica", 18))
        void = tk.Label(window, text=f"")
        tempareture = customtkinter.CTkLabel(window, text=f"A jelenlegi hőmérséklet: {jsonformatum['main']['temp']} °C", font=("Helvetica", 18))
        tempareture_feels = customtkinter.CTkLabel(window, text=f"A jelenlegi hőérzet: {jsonformatum['main']['feels_like']} °C", font=("Helvetica", 18))
        if jsonformatum['weather'][0]['description'] == "clear sky":
            sky = customtkinter.CTkLabel(window, text=f"Az ég tiszta", font=("Helvetica", 18))
        if jsonformatum['weather'][0]['description'] == "few clouds":
            sky = customtkinter.CTkLabel(window, text=f"Néhány felhő van az égen", font=("Helvetica", 18))
        else:
            sky = customtkinter.CTkLabel(window, text=f"Az ég: {jsonformatum['weather'][0]['description']}", font=("Helvetica",18))
        
        if jsonformatum['wind']['speed'] == 0:
            wind = customtkinter.CTkLabel(window, text=f"Jelenleg nincs szél", font=("Helvetica", 18))
        else:
            wind = customtkinter.CTkLabel(window, text=f"A szél sebessége: {jsonformatum['wind']['speed']} m/s", font=("Helvetica", 18))
        humadity = customtkinter.CTkLabel(window, text=f"A jelenlegi páratartartalom: {jsonformatum['main']['humidity']} %", font=("Helvetica", 18))
        if jsonformatum['cod'] == 404:
            print("Adj meg létező várost")
        if KeyError == 'name':
            print("Adj meg létező várost")
        message.pack()
        message.place(relx=0.1, rely=0.2)
        #void.pack()
        tempareture.pack()
        tempareture.place(relx=0.1, rely=0.4)
        tempareture_feels.pack()
        tempareture_feels.place(relx=0.1, rely=0.5)
        sky.pack()
        sky.place(relx=0.1, rely=0.6)
        wind.pack()
        wind.place(relx=0.1, rely=0.7)
        humadity.pack()
        humadity.place(relx=0.1, rely=0.8)
        
        def save_data():
            con = sqlite3.connect("weather.db")
            cur = con.cursor()
            nowtime = strftime("%m-%d || %H:%M:%S", gmtime())
            try:
                cur.execute("CREATE TABLE weather(time ,city, temp, feels_like, sky_description, wind_speed, humidity)")
            except:
                pass
            ins = cur.execute(f"insert into weather(time, city, temp, feels_like, sky_description, wind_speed, humidity) values ('{nowtime}','{jsonformatum['name']}','{jsonformatum['main']['temp']}', '{jsonformatum['main']['feels_like']}', '{jsonformatum['weather'][0]['description']}', '{jsonformatum['wind']['speed']}', '{jsonformatum['main']['humidity']}')")
            con.commit()
            cur.execute("SELECT city FROM weather;")
            name = cur.fetchone()
            print(name)
        save = customtkinter.CTkButton(master=window,
                                    width=120,
                                    height=32,
                                    border_width=0,
                                    corner_radius=10,
                                    text="Adatok mentése!",
                                    hover_color="lightblue",
                                    command=save_data)
        save.place(relx=0.14, rely=0.1)
        
        
        def remover():
            humadity.place_forget()
            message.place_forget()
            tempareture.place_forget()
            tempareture_feels.place_forget()
            sky.place_forget()
            wind.place_forget()
            humadity.place_forget()
            hider.place_forget()
        hider = customtkinter.CTkButton(master=window,
                                    width=120,
                                    height=32,
                                    border_width=0,
                                    corner_radius=10,
                                    text="Eltüntetés",
                                    hover_color="lightblue",
                                    command=remover)
        hider.pack
        hider.place(relx=0.7, rely=0.1)
        
    label.pack()
    text_entry.place(relx=0.4, rely=0.1)
    button = customtkinter.CTkButton(master=window,
                                    width=120,
                                    height=32,
                                    border_width=0,
                                    corner_radius=10,
                                    text="Keresés",
                                    hover_color="lightblue",
                                    command=submit_input)

    button.place(relx=0.7, rely=0.1)
    #photo = PhotoImage("weather.png")
    #window.iconbitmap("weather.ico")

    def mapopen():
        #marker_1 = map_widget.set_address(varosformap, marker=True)
        #marker_1.set_text(f"{jsonformatumformap['main']['temp']} °C")  
        
        varosformap = text_entry.get()
        lekerdez = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={varosformap}&appid=a3c3ac028697416ece9bd3c3a7c0f500&units=metric')
        jsonformatumformap = json.loads(lekerdez.text)
        map_widget = tkintermapview.TkinterMapView(window, width=600, height=400, corner_radius=0)
        map_widget.place(relx=0.5, rely=0.3)
        map_widget.set_address("budapest")
        marker_1 = map_widget.set_address(varosformap, marker=True)
        marker_1.set_text(f"{jsonformatumformap['main']['temp']} °C")
        #map_widget.zoom()
        """def slider_event(value):
            print(value)
        slider = customtkinter.CTkSlider(master=window,
                                        width=160,
                                        height=16,
                                        border_width=5.5,
                                        command=slider_event)
        slider.place(relx=0.5, rely=0.9)
        slider.pack()"""
        
    mapbtn = customtkinter.CTkButton(master=window,
                                    width=120,
                                    height=32,
                                    border_width=0,
                                    corner_radius=10,
                                    text="Megjelenítés térképen",
                                    hover_color="lightblue",
                                    command=mapopen)
    mapbtn.place(relx=0.7, rely=0.2)


    window.mainloop()
except KeyboardInterrupt:
    print("Kilépés")
    exit()
