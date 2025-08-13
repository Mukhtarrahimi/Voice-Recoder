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

# logo
photo = PhotoImage(file="Record.png")
Label(root, image=photo, bg="#4a4a4a").pack(pady=20)

# name
Label(text="Voice Recorder", font=("Arial", 30, "bold"), bg="#4a4a4a", fg="white").pack()

# entry box
duration = StringVar()
Entry(root, textvariable=duration, font=("Arial", 20), width=15).pack(pady=10)
Label(text="Enter Duration in seconds", font=("Arial", 15), bg="#4a4a4a", fg="white").pack()

# button
record = Button(root, text="Record", font=("Arial", 20), bg="#111111", fg="white", border=0, command=Record).pack(pady=20)




root.mainloop()
