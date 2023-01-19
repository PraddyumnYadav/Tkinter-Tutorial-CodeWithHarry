# https://www.youtube.com/watch?v=dizKSszF74A&list=PLu0W_9lII9ajLcqRcj4PoEihkukF_OTzA&index=5
# Importing Essentials
from tkinter import Tk
from tkinter import Label

# Creating Our Root Window
root = Tk()

# Set Default Size of Our Tkinter Window - (WidthxHeight)
root.geometry("444x234")

# Set Minimum Size of Our Window - (Width, Height)
root.minsize(300, 200)

# Set Maximum Size of Our Window - (Width, Height)
root.maxsize(800, 600)

# Add a Label to Our Tkinter GUI
gui_label = Label(text="Hey Every One This is My GUI with Tkinter.")
gui_label.pack()

# Starting MainLoop
root.mainloop()
