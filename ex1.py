# Exercise of https://www.youtube.com/watch?v=end4IWH0ihY&list=PLu0W_9lII9ajLcqRcj4PoEihkukF_OTzA&index=6
# Importing Essentials
import os
from tkinter import Tk, Label, PhotoImage

# Initialize Tk root Class
root = Tk()

# Set Default Size of Our Tkinter Window - (WidthxHeight)
root.geometry("200x600")

# Set Minimum Size of Our Window - (Width, Height)
root.minsize(350, 200)

# Add a Label
WelcomeLabel = Label(text="All Images of This Folder")
WelcomeLabel.pack()

# Get All PNG Files in a List name pngFiles
pngFiles = []
for item in os.listdir():
    if item.endswith(".png"):
        pngFiles.append(item)
print(pngFiles)

# Display All The PNG files to our GUI Screen
i = 0
pics = []
for file in pngFiles:
    pics.append(PhotoImage(file=file))
    Label(root, image=pics[i]).pack()
    i += 1

# Run The MainLoop
root.mainloop()
