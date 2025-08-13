from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import 
import time
import wavio as wv
# functions
def Record():
    freq = 44100
    dur = int(duration.get())
    recording = sound.rec(int(dur * freq), samplerate=freq, channels=2)
    # timer
    try:
        temp = int(duration.get())
    except:
        print("Please Enter the right value")
    
    while temp > 0:
        root.update()
        time.sleep(1)
        time -= 1
    
    if (temp == 0):
        messagebox.showinfo("Time Countdown", "Tims's up")
    Label(text=f"{str(temp)}", font="arial, 40", width=4, background="#4a4a4a").place(x=240, y=5)
    sound.wait()
    write("recording.wav", freq, recording)


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
