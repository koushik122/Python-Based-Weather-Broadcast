from tkinter import *
from PIL import Image, ImageTk

root=Tk()

# Geometry(WxH)
root.geometry("760x450")
root.title("Weather App")

# Changed resizability
root.resizable(width=False,height=False)
# Background colour update
root.config(bg="#47ceff")


# Search Bar
image=Image.open("App icon resources/Search Bar.png")
# (W,H)
resized_image=image.resize((300,130))
im=ImageTk.PhotoImage(resized_image)
Label(image=im,bg="#47ceff").place(x=235,y=34)




root.mainloop()