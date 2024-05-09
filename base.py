from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
from timezonefinder import TimezoneFinder 
import datetime
import pytz
import requests
import cred


obj = TimezoneFinder()
def search():
  city=entry.get()
  url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={cred.api_key}"
  res=requests.get(url)
  response=res.json()
  if res.status_code>=200 and res.status_code<=299:
    icon= (response['weather'][0]['icon'])
    icon_name=f"{icon}@2x.png"
    icon_image=ctk.CTkImage(light_image=Image.open(f"Weather Condition Icons/{icon_name}"),size=(150, 150))
    icon_lable.configure(image=icon_image)

    lng=response['coord']['lon']
    lat=response['coord']['lat']
    timezone=obj.timezone_at(lng=lng, lat=lat)
    utc_now = datetime.datetime.now()
    timezone = pytz.timezone(timezone)
    local_now = utc_now.astimezone(timezone)
    time = local_now.strftime("%I:%M %p")
    
    time_lable.configure(text=time)
  else:
    tkinter.messagebox.showwarning("No Result",  "-Enter valid city name\n-Check your internet connection")


root =ctk.CTk()

# Geometry (Width x Height)
root.geometry("760x500")
root.title("Weather App")

# Disallow resizing
root.resizable(width=False, height=False)

# Background colour
root.config(bg="#47ceff")


# Search Bar Entry
entry = ctk.CTkEntry(root,width=366,height=55, corner_radius=30, 
                     placeholder_text="Enter City Name", font=('Arial', 27),
                       bg_color="#47ceff", fg_color="#000", justify=CENTER)
entry.place(x=200,y=60)

# Search icon image
search_icon_image = ctk.CTkImage(dark_image=Image.open("App icon resources/Search_icon.png"),size=(35, 35))
button = ctk.CTkButton(root, image=search_icon_image,text="",
                       width=33,corner_radius=90,height=55,
                        fg_color="#000",bg_color="#47ceff",
                         command=search)
button.place(x=570,y=60)

#Weather Detail 
canvas=Canvas(root,bg="black",highlightbackground="black",height=210,width=200)
canvas.pack(side='left',padx=10)

label1 = ctk.CTkLabel(canvas, text="Humidity:", fg_color="black", text_color="white")
label1.place(x=10,y=12)
label2 = ctk.CTkLabel(canvas, text="Wind Speed:", fg_color="black", text_color="white")
label2.place(x=10,y=42)
label3 = ctk.CTkLabel(canvas, text="AQI:", fg_color="black", text_color="white")
label3.place(x=10,y=72)
label4 = ctk.CTkLabel(canvas, text="Pressure:", fg_color="black", text_color="white")
label4.place(x=10,y=102)
label5 = ctk.CTkLabel(canvas, text="Visibility:", fg_color="black", text_color="white")
label5.place(x=10,y=132)

Humidity_variable = ctk.StringVar()
Wind_Speed_variable = ctk.StringVar()
AQI_variable = ctk.StringVar()
Pressure_variable = ctk.StringVar()
Visibility_variable = ctk.StringVar()


t_label1 = ctk.CTkLabel(canvas, textvariable=Humidity_variable, fg_color="black", text_color="white")
t_label1.place(x=90,y=12)

t_label2 = ctk.CTkLabel(canvas, textvariable=Wind_Speed_variable, fg_color="black", text_color="white")
t_label2.place(x=90,y=42)

t_label3 = ctk.CTkLabel(canvas, textvariable=AQI_variable, fg_color="black", text_color="white")
t_label3.place(x=90,y=72)

t_label4 = ctk.CTkLabel(canvas, textvariable=Pressure_variable, fg_color="black", text_color="white")
t_label4.place(x=90,y=102)

t_label5 = ctk.CTkLabel(canvas, textvariable=Visibility_variable, fg_color="black", text_color="white")
t_label5.place(x=90,y=132)





#icon label
icon_lable = ctk.CTkLabel(root,text="", bg_color='#47ceff')
icon_lable.place(x=500,y=200)


# Time date lable
time_lable = ctk.CTkLabel(root,text="",text_color='#fff', bg_color='#47ceff', font=('Arial', 27))
time_lable.place(x=5,y=3)


root.mainloop()
