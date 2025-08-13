from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Voice Recorder")
root.geometry("600x700+400+80")
root.resizable(False, False)
root.configure(background="#4a4a4a")

# icon
image_icon = PhotoImage(file="Record.png")
root.iconphoto(False, image_icon)

root.mainloop()