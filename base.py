from tkinter import *
from PIL import Image, ImageTk


def search():
    print("Search button clicked!")


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





root.mainloop()
