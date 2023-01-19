# https://www.youtube.com/watch?v=end4IWH0ihY&list=PLu0W_9lII9ajLcqRcj4PoEihkukF_OTzA&index=6
# Importing Essentials
from tkinter import Tk, Label, PhotoImage

# Creating Our Root Window
root = Tk()

# Set Default Size of Our Tkinter Window - (WidthxHeight)
root.geometry("444x234")

# Set Minimum Size of Our Window - (Width, Height)
root.minsize(300, 200)

# Set Maximum Size of Our Window - (Width, Height)
root.maxsize(800, 600)

# Add a Label to Our Tkinter GUI
gui_label = Label(text="Adding Image in GUI with Tkinter.")
gui_label.pack()

# Add Image to Our Tkinter GUI
photo = PhotoImage(file="lion.png")
img_label = Label(image=photo)
img_label.pack()

# Starting MainLoop
root.mainloop()
