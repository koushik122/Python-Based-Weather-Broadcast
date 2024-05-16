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
    date = local_now.strftime("%a, %d %b")
    
    time_lable.configure(text=time)
    date_lable.configure(text=date)

    temp=f"{str(round(float(response['main']['temp'])))}°C"
    tempareture.set(temp)

    feels_like_temp=f"Feels Like {str(round(float(response['main']['feels_like'])))}°C"
    fl_temp.set(feels_like_temp)

    description = (response['weather'][0]['description'])
    icon_lable_variable.set(description.title())

# Weather deta call
    aqi_url=f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lng}&lon={lat}&appid={cred.api_key}"
    aqi_response=requests.get(aqi_url).json()
    humi= f"{(response['main']['humidity'])}%"
    wind= f"{(response['wind']['speed'])} m/s"
    aqi= str(aqi_response['list'][0]['main']['aqi'])
    pre=f"{(response['main']['pressure'])} hPa"
    vis=f"{str(int(response['visibility'])/1000)} km"

    Humidity_variable.set(humi)
    Wind_Speed_variable.set(wind)
    
    Pressure_variable.set(pre)
    Visibility_variable.set(vis)
    match aqi:
      case "1":
        AQI_variable.set("Good")
      case "2":
        AQI_variable.set("Fair")
      case "3":
        AQI_variable.set("Moderate")
      case "4":
        AQI_variable.set("Poor")
      case "5":
        AQI_variable.set("Very Poor")
      case _:
        AQI_variable.set("No value")  


  else:
    tkinter.messagebox.showwarning("No Result",  "-Enter valid city name\n-Check your internet connection")

def on_click(event):
  search()

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
                       bg_color="#47ceff", fg_color="#000",text_color='#fff', justify=CENTER)
entry.place(x=200,y=60)
entry.bind('<Return>', on_click)

# Search icon image
search_icon_image = ctk.CTkImage(dark_image=Image.open("App icon resources/Search_icon.png"),size=(35, 35))
button = ctk.CTkButton(root, image=search_icon_image,text="",
                       width=33,corner_radius=90,height=55,
                        fg_color="#000",bg_color="#47ceff",
                         command=search)
button.place(x=570,y=60)

# Weather Detail  
canvas=Canvas(root,bg="#47ceff",highlightbackground="#47ceff",height=210,width=200)
canvas.place(x=10,y=200)

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

my_rectangle = round_rectangle(4, 4, 200, 210, radius=20, fill="black")


# Weather details lables
label1 = ctk.CTkLabel(canvas, text="Humidity:", fg_color="black",bg_color="black", text_color="white")
label1.place(x=10,y=12)
label2 = ctk.CTkLabel(canvas, text="Wind Speed:", fg_color="black",bg_color="black", text_color="white")
label2.place(x=10,y=42)
label3 = ctk.CTkLabel(canvas, text="AQI:", fg_color="black",bg_color="black", text_color="white")
label3.place(x=10,y=72)
label4 = ctk.CTkLabel(canvas, text="Pressure:", fg_color="black",bg_color="black", text_color="white")
label4.place(x=10,y=102)
label5 = ctk.CTkLabel(canvas, text="Visibility:", fg_color="black",bg_color="black", text_color="white")
label5.place(x=10,y=132)

Humidity_variable = ctk.StringVar()
Wind_Speed_variable = ctk.StringVar()
AQI_variable = ctk.StringVar()
Pressure_variable = ctk.StringVar()
Visibility_variable = ctk.StringVar()

# Weather details value lables
t_label1 = ctk.CTkLabel(canvas, textvariable=Humidity_variable, fg_color="black",bg_color="black", text_color="white")
t_label1.place(x=90,y=12)

t_label2 = ctk.CTkLabel(canvas, textvariable=Wind_Speed_variable, fg_color="black",bg_color="black", text_color="white")
t_label2.place(x=90,y=42)

t_label3 = ctk.CTkLabel(canvas, textvariable=AQI_variable, fg_color="black",bg_color="black", text_color="white")
t_label3.place(x=90,y=72)

t_label4 = ctk.CTkLabel(canvas, textvariable=Pressure_variable, fg_color="black",bg_color="black", text_color="white")
t_label4.place(x=90,y=102)

t_label5 = ctk.CTkLabel(canvas, textvariable=Visibility_variable, fg_color="black",bg_color="black", text_color="white")
t_label5.place(x=90,y=132)

t_label1 = ctk.CTkLabel(canvas, textvariable=Humidity_variable, fg_color="black",bg_color="black", text_color="white")
t_label1.place(x=90,y=12)


# Tempareture lable
tempareture = ctk.StringVar()
temp_lable = ctk.CTkLabel(root,textvariable=tempareture, bg_color='#47ceff',text_color='#fff', font=('Arial', 45))
temp_lable.place(x=330,y=200)

fl_temp = ctk.StringVar()
fl_temp_lable = ctk.CTkLabel(root,textvariable=fl_temp, bg_color='#47ceff',text_color='#fff', font=('Arial', 23))
fl_temp_lable.place(x=300,y=250)


# Icon label
icon_lable = ctk.CTkLabel(root,text="", bg_color='#47ceff')
icon_lable.place(x=500,y=160)

# Icon lable description
icon_lable_variable = ctk.StringVar()
icon_lable_description = ctk.CTkLabel(root,textvariable=icon_lable_variable,width=230, bg_color='#47ceff',text_color='#fff',justify= "center", font=('Arial', 24, 'bold'))
icon_lable_description.place(x=467,y=290)


# Time date lable
time_lable = ctk.CTkLabel(root,text="",text_color='#262e94', bg_color='#47ceff', font=('Arial', 25))
time_lable.place(x=5,y=3)

date_lable = ctk.CTkLabel(root,text="",text_color='#262e94', bg_color='#47ceff', font=('Arial', 25))
date_lable.place(x=5,y=28)

root.mainloop()
