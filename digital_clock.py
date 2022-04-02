from time import strftime
import tkinter
from tkinter import Tk

root = Tk()

root.title("Digital Clock")

root.geometry("235x60")

clock = tkinter.Label(root, fg="black", font=("Arial", 30, 'bold'))

clock.place(x=0, y=0)


def digital_clock():
    time = strftime('%H: %M: %S')

    clock.configure(text=time)

    clock.after(1000, digital_clock)

digital_clock()

root.mainloop()
