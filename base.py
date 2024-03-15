from tkinter import *
from PIL import Image, ImageTk


def search():
    city=city_name.get()
    print("Search button clicked!\nThe city is", city)


root = Tk()

# Geometry (Width x Height)
root.geometry("760x500")
root.title("Weather App")

# Disallow resizing
root.resizable(width=False, height=False)

# Background colour
root.config(bg="#47ceff")


# Search Bar image
search_bar_image = Image.open("App icon resources/Search Bar.png")
# (Width x Height)
resized_search_bar_image = search_bar_image.resize((300, 130))
search_bar_photo = ImageTk.PhotoImage(resized_search_bar_image)
Label(root, image=search_bar_photo, bg="#47ceff", highlightthickness=0).place(x=235, y=34)

# Search icon image
search_icon_image = Image.open("App icon resources/Search icon.png")
resized_search_icon_image = search_icon_image.resize((35,35))
search_icon_photo = ImageTk.PhotoImage(resized_search_icon_image)
Button(root, image=search_icon_photo, command=search, bg="#000000", bd=0, highlightthickness=0
).place(x=480, y=82)


# Variable for storing city
city_name = StringVar()

Entry(root, textvariable=city_name,bg="#000000",bd=0,fg="#ffffff",width=16,justify=CENTER,
       cursor='xterm',insertbackground='white',font=('Arial 18 bold')).place(x=267,y=85)





root.mainloop()
