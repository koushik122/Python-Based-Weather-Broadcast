from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk


def search():
    city=entry.get()
    print("Search button clicked!\nThe city is", city)


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
canvas=Canvas(root,bg="black",highlightbackground="black",height=180,width=200)
canvas.pack(side='left',padx=10)

label1 = ctk.CTkLabel(canvas, text="Humidity:", fg_color="black", text_color="white")
label1.place(x=10,y=20)
label2 = ctk.CTkLabel(canvas, text="Wind Speed:", fg_color="black", text_color="white")
label2.place(x=10,y=50)
label3 = ctk.CTkLabel(canvas, text="AQI:", fg_color="black", text_color="white")
label3.place(x=10,y=80)
label4 = ctk.CTkLabel(canvas, text="Pressure:", fg_color="black", text_color="white")
label4.place(x=10,y=110)
label5 = ctk.CTkLabel(canvas, text="Visibility:", fg_color="black", text_color="white")
label5.place(x=10,y=140)

Humidity_variable = ctk.StringVar()
Wind_Speed_variable = ctk.StringVar()
AQI_variable = ctk.StringVar()
Pressure_variable = ctk.StringVar()
Visibility_variable = ctk.StringVar()


label1 = ctk.CTkLabel(canvas, textvariable=Humidity_variable, fg_color="black", text_color="white")
label1.place(x=90,y=20)

label1 = ctk.CTkLabel(canvas, textvariable=Wind_Speed_variable, fg_color="black", text_color="white")
label1.place(x=90,y=50)

label1 = ctk.CTkLabel(canvas, textvariable=AQI_variable, fg_color="black", text_color="white")
label1.place(x=90,y=80)

label1 = ctk.CTkLabel(canvas, textvariable=Pressure_variable, fg_color="black", text_color="white")
label1.place(x=90,y=110)

label1 = ctk.CTkLabel(canvas, textvariable=Visibility_variable, fg_color="black", text_color="white")
label1.place(x=90,y=140)





#icon label
label1 = ctk.CTkLabel(root, text="Humidity:", fg_color="black", text_color="white")
label1.place(x=500,y=200)




root.mainloop()
