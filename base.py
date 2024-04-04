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





root.mainloop()
