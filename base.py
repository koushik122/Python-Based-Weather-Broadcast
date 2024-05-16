from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
from timezonefinder import TimezoneFinder 
import datetime
import pytz
import requests
import cred
import detailed_desc

obj = TimezoneFinder()

def search():
  city=entry.get()
  url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={cred.api_key}"
  api_response=requests.get(url)
  global local_now
  if api_response.status_code>=200 and api_response.status_code<=299:
    response=api_response.json()
    longitude=response['coord']['lon']
    latitude=response['coord']['lat']
    timezone_str=obj.timezone_at(lng=longitude, lat=latitude)
    utc_now = datetime.datetime.now()
    timezone = pytz.timezone(timezone_str)
    local_now = utc_now.astimezone(timezone)

    icon = (response['weather'][0]['icon'])
    icon_name=f"{icon}@2x.png"
    icon_image=ctk.CTkImage(light_image=Image.open(f"Weather Condition Icons/{icon_name}"),size=(140, 140))
    icon_lable.configure(image=icon_image)

    time = local_now.strftime("%I:%M %p")
    date = local_now.strftime("%a, %d %b")
    
    time_lable.configure(text=time)
    date_lable.configure(text=date)
    timezone_variable.set(timezone_str)

    temp=f"{str(round(float(response['main']['temp'])))}°C"
    tempareture.set(temp)

    feels_like_temp=f"Feels Like {str(round(float(response['main']['feels_like'])))}°C"
    fl_temp.set(feels_like_temp)

    description = (response['weather'][0]['description'])
    icon_lable_variable.set(description.title())

    details = int(response['weather'][0]['id'])
    detailed = detailed_desc.id_to_weather[details]
    id_lable_text = f"Detailed Description :\n{detailed.title()}"
    id_lable.configure(text=id_lable_text)


# AQI API call
    aqi_url=f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={cred.api_key}"
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

    weekday_button_name_change()
    forecast_api_call()
    today()

  else:
    tkinter.messagebox.showwarning("No Result",  "-Enter valid city name\n-Check your internet connection")

# To make rounded corner canvas
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

def round_rectangle_forecast(x1, y1, x2, y2, radius=25, **kwargs):
        
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

    return Canvas.create_polygon(points, **kwargs, smooth=True)

def on_press(event):
  search()

def forecast_api_call():
  global forecast_response
  city=entry.get()
  forecast_url=f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={cred.api_key}"
  forecast_api_response=requests.get(forecast_url)
  if forecast_api_response.status_code>=200 and forecast_api_response.status_code<=299:
    forecast_response=forecast_api_response.json()

  else:
    tkinter.messagebox.showwarning("Failed To Load Forecast Data",  "-Enter valid city name\n-Check your internet connection")


def weekday_button_name_change():
  global today_date
  global first_date
  global second_date
  global third_date
  global forth_date
  global fifth_date
  today = local_now.today()

  first_day_datetime = today + datetime.timedelta(days=1)
  second_day_datetime = today + datetime.timedelta(days=2)
  third_day_datetime = today + datetime.timedelta(days=3)
  forth_day_datetime = today + datetime.timedelta(days=4)
  fifth_day_datetime = today + datetime.timedelta(days=5)

  # Weekday button name change
  day_1_button.configure(text=first_day_datetime.strftime("%A"))
  day_2_button.configure(text=second_day_datetime.strftime("%A"))
  day_3_button.configure(text=third_day_datetime.strftime("%A"))
  day_4_button.configure(text=forth_day_datetime.strftime("%A"))
  day_5_button.configure(text=fifth_day_datetime.strftime("%A"))

  # Next 5 days date including today
  today_date=local_now.strftime("%Y-%m-%d")
  first_date=first_day_datetime.strftime("%Y-%m-%d")
  second_date=second_day_datetime.strftime("%Y-%m-%d")
  third_date=third_day_datetime.strftime("%Y-%m-%d")
  forth_date=forth_day_datetime.strftime("%Y-%m-%d")
  fifth_date=fifth_day_datetime.strftime("%Y-%m-%d")

def convert_time_to_12hr_format(time_str):
  time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S")
  return time_obj.strftime("%I %p").lstrip('0')

def make_rectangle(weather_count):
  left, top, rignt, bottom = 20,20,150,180
  for i in range(weather_count):
    round_rectangle_forecast(left, top, rignt, bottom, fill='green')
    left+=150
    rignt+=150

def clear(Canvas):
  Canvas.delete("all")
  for label in labels:
    label.destroy()
  labels.clear()

def today():
  clear(Canvas)
  target_date = today_date
  weather_updates_count = 0
  
  x_value, y_value = 20,20
  for item in forecast_response['list']:
    date = item['dt_txt'].split(' ')[0]
    if date == target_date:
        weather_updates_count += 1
        time = item['dt_txt'].split(' ')[1]
        weather_f_des_str=(item['weather'][0]['description'])
        tempareture_str=f"{str(round(float(item['main']['temp'])))}°C"
        time_str=convert_time_to_12hr_format(time)
        combi_text=f"{(weather_f_des_str.title())}\n{tempareture_str}\n\n{time_str}"
        icon = (item['weather'][0]['icon'])
        icon_name=f"{icon}@2x.png"
        icon_image=ctk.CTkImage(light_image=Image.open(f"Weather Condition Icons/{icon_name}"),size=(50,50))
        forecast_lables=ctk.CTkLabel(Canvas,width=100,image=icon_image,text=combi_text,text_color="white",bg_color="green",compound="top")
        forecast_lables.place(x = x_value,y = y_value)
        labels.append(forecast_lables)
        x_value += 120

  make_rectangle(weather_updates_count)
 

def day_1():
  clear(Canvas)
  target_date=first_date
  weather_updates_count = 8
  
  x_value, y_value = 20,20
  for item in forecast_response['list']:
    date = item['dt_txt'].split(' ')[0]
    if date == target_date:
        time = item['dt_txt'].split(' ')[1]
        weather_f_des_str=(item['weather'][0]['description'])
        tempareture_str=f"{str(round(float(item['main']['temp'])))}°C"
        time_str=convert_time_to_12hr_format(time)
        combi_text=f"{(weather_f_des_str.title())}\n{tempareture_str}\n\n{time_str}"
        icon = (item['weather'][0]['icon'])
        icon_name=f"{icon}@2x.png"
        icon_image=ctk.CTkImage(light_image=Image.open(f"Weather Condition Icons/{icon_name}"),size=(50,50))
        forecast_lables=ctk.CTkLabel(Canvas,width=100,image=icon_image,text=combi_text,bg_color="green",compound="top")
        forecast_lables.place(x = x_value,y = y_value)
        labels.append(forecast_lables)
        x_value+=120

  make_rectangle(weather_updates_count)


def day_2():
  clear(Canvas)
  target_date=second_date
  weather_updates_count = 8
  
  x_value, y_value = 20,20
  for item in forecast_response['list']:
    date = item['dt_txt'].split(' ')[0]
    if date == target_date:
        time = item['dt_txt'].split(' ')[1]
        weather_f_des_str=(item['weather'][0]['description'])
        tempareture_str=f"{str(round(float(item['main']['temp'])))}°C"
        time_str=convert_time_to_12hr_format(time)
        combi_text=f"{(weather_f_des_str.title())}\n{tempareture_str}\n\n{time_str}"
        icon = (item['weather'][0]['icon'])
        icon_name=f"{icon}@2x.png"
        icon_image=ctk.CTkImage(light_image=Image.open(f"Weather Condition Icons/{icon_name}"),size=(50,50))
        forecast_lables=ctk.CTkLabel(Canvas,width=100,image=icon_image,text=combi_text,bg_color="green",compound="top")
        forecast_lables.place(x = x_value,y = y_value)
        labels.append(forecast_lables)
        x_value+=120

  make_rectangle(weather_updates_count)
 

def day_3():
  clear(Canvas)
  target_date=third_date
  weather_updates_count = 8
  
  x_value, y_value = 20,20
  for item in forecast_response['list']:
    date = item['dt_txt'].split(' ')[0]
    if date == target_date:
        time = item['dt_txt'].split(' ')[1]
        weather_f_des_str=(item['weather'][0]['description'])
        tempareture_str=f"{str(round(float(item['main']['temp'])))}°C"
        time_str=convert_time_to_12hr_format(time)
        combi_text=f"{(weather_f_des_str.title())}\n{tempareture_str}\n\n{time_str}"
        icon = (item['weather'][0]['icon'])
        icon_name=f"{icon}@2x.png"
        icon_image=ctk.CTkImage(light_image=Image.open(f"Weather Condition Icons/{icon_name}"),size=(50,50))
        forecast_lables=ctk.CTkLabel(Canvas,width=100,image=icon_image,text=combi_text,bg_color="green",compound="top")
        forecast_lables.place(x = x_value,y = y_value)
        labels.append(forecast_lables)
        x_value+=120

  make_rectangle(weather_updates_count)
 

def day_4():
  clear(Canvas)
  target_date=forth_date
  weather_updates_count = 8
  
  x_value, y_value = 20,20
  for item in forecast_response['list']:
    date = item['dt_txt'].split(' ')[0]
    if date == target_date:
        time = item['dt_txt'].split(' ')[1]
        weather_f_des_str=(item['weather'][0]['description'])
        tempareture_str=f"{str(round(float(item['main']['temp'])))}°C"
        time_str=convert_time_to_12hr_format(time)
        combi_text=f"{(weather_f_des_str.title())}\n{tempareture_str}\n\n{time_str}"
        icon = (item['weather'][0]['icon'])
        icon_name=f"{icon}@2x.png"
        icon_image=ctk.CTkImage(light_image=Image.open(f"Weather Condition Icons/{icon_name}"),size=(50,50))
        forecast_lables=ctk.CTkLabel(Canvas,width=100,image=icon_image,text=combi_text,bg_color="green",compound="top")
        forecast_lables.place(x = x_value,y = y_value)
        labels.append(forecast_lables)
        x_value+=120

  make_rectangle(weather_updates_count)
 

def day_5():
  clear(Canvas)
  target_date=fifth_date
  weather_updates_count = 0
  
  x_value, y_value = 20,20
  for item in forecast_response['list']:
    date = item['dt_txt'].split(' ')[0]
    if date == target_date:
        weather_updates_count += 1
        time = item['dt_txt'].split(' ')[1]
        weather_f_des_str=(item['weather'][0]['description'])
        tempareture_str=f"{str(round(float(item['main']['temp'])))}°C"
        time_str=convert_time_to_12hr_format(time)
        combi_text=f"{(weather_f_des_str.title())}\n{tempareture_str}\n\n{time_str}"
        icon = (item['weather'][0]['icon'])
        icon_name=f"{icon}@2x.png"
        icon_image=ctk.CTkImage(light_image=Image.open(f"Weather Condition Icons/{icon_name}"),size=(50,50))
        forecast_lables=ctk.CTkLabel(Canvas,width=100,image=icon_image,text=combi_text,bg_color="green",compound="top")
        forecast_lables.place(x = x_value,y = y_value)
        labels.append(forecast_lables)
        x_value+=120

  make_rectangle(weather_updates_count)
 

root = ctk.CTk()

# Geometry (Width x Height)
root.geometry("980x550")
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
entry.bind('<Return>', on_press)

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

# Created rounded rectangle
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


# Tempareture lable
tempareture = ctk.StringVar()
temp_lable = ctk.CTkLabel(root,textvariable=tempareture, bg_color='#47ceff',text_color='#fff', font=('Arial', 45))
temp_lable.place(x=320,y=200)

fl_temp = ctk.StringVar()
fl_temp_lable = ctk.CTkLabel(root,textvariable=fl_temp, bg_color='#47ceff',text_color='#fff', font=('Arial', 23))
fl_temp_lable.place(x=290,y=250)


# Icon label
icon_lable = ctk.CTkLabel(root,text="",bg_color='#47ceff')
icon_lable.place(x=510,y=160)

# Icon lable description
icon_lable_variable = ctk.StringVar()
icon_lable_description = ctk.CTkLabel(root,textvariable=icon_lable_variable,width=250, bg_color='#47ceff',text_color='#fff',justify= "center", font=('Arial', 24))
icon_lable_description.place(x=460,y=280)

# Detailed weather description lable
id_lable = ctk.CTkLabel(root,text="",width=230, bg_color='#47ceff',text_color='#fff',justify= "center", font=('Arial', 20))
id_lable.place(x=700,y=200)

# Time date lable
time_lable = ctk.CTkLabel(root,text="",text_color='#262e94', bg_color='#47ceff', font=('Arial', 25))
time_lable.place(x=7,y=3)

date_lable = ctk.CTkLabel(root,text="",text_color='#262e94', bg_color='#47ceff', font=('Arial', 25))
date_lable.place(x=7,y=28)

# Timezone lable
timezone_variable = ctk.StringVar()
timezone_lable = ctk.CTkLabel(root, textvariable=timezone_variable, text_color='#262e94', bg_color='#47ceff', font=('Arial', 25))
timezone_lable.place(x=790,y=10)


# Canvas for weather forecast
# scrollregion = (1eft, top, right, bottom) 
Canvas = Canvas(root,height=200, bg="black")
Canvas.pack(expand=True, anchor='sw', fill=X)

# To store labels for forecast
labels=[]

today_button=ctk.CTkButton(root,width=80, text="Today",bg_color="#47ceff",corner_radius=5, font=('Arial', 16), command = today)
today_button.place(x=50,y=350)

day_1_button=ctk.CTkButton(root,width=100, text="Day 1",bg_color="#47ceff",corner_radius=5, font=('Arial', 16),command = day_1)
day_1_button.place(x=180,y=350)

day_2_button=ctk.CTkButton(root,width=100, text="Day 2",bg_color="#47ceff",corner_radius=5, font=('Arial', 16),command = day_2)
day_2_button.place(x=340,y=350)

day_3_button=ctk.CTkButton(root, width = 100, text = "Day 3",bg_color="#47ceff",corner_radius=5, font=('Arial', 16),command = day_3)
day_3_button.place(x=500,y=350)

day_4_button=ctk.CTkButton(root,width=100, text="Day 4",bg_color="#47ceff",corner_radius=5, font=('Arial', 16),command=day_4)
day_4_button.place(x=660,y=350)

day_5_button=ctk.CTkButton(root,width=100, text="Day 5",bg_color="#47ceff",corner_radius=5, font=('Arial', 16),command=day_5)
day_5_button.place(x=820,y=350)


root.mainloop()