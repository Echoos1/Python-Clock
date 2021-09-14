from tkinter import *
import time

root = Tk()
root.title("Clock")


def edit():
    t = time.localtime()
    secs = time.strftime("%S", t)
    mins = time.strftime("%M", t)
    hour = time.strftime("%H", t)
    day = time.strftime("%d", t)
    mth = time.strftime("%m", t)
    year = time.strftime("%y", t)
    canvas.coords(secbar, 0, 0, (float(secs) * (300 / 59)), 50)
    canvas.itemconfig(sectxt, text=secs)
    canvas.coords(minbar, 0, 50, (float(mins) * (300 / 59)), 100)
    canvas.itemconfig(mintxt, text=mins)
    canvas.coords(hourbar, 0, 100, (float(hour) * (300 / 23)), 150)
    canvas.itemconfig(hourtxt, text=time.strftime("%I %p", t))
    canvas.coords(daybar, 0, 150, (float(day) * (300 / 30.5)), 200)
    canvas.itemconfig(daytxt, text=day)
    canvas.coords(mthbar, 0, 200, (float(mth) * (300 / 12)), 250)
    canvas.itemconfig(mthtxt, text=(time.strftime("%B", t)))
    canvas.coords(yearbar, 0, 250, (float(year) * (300 / 99)), 300)
    canvas.itemconfig(yeartxt, text=time.strftime("%Y", t))
    root.after(200, edit)

canvas = Canvas(root, bg="white", height=300, width=300)
canvas.pack()

secbar = canvas.create_rectangle(0,0,0,50, fill="cyan")
sectxt = canvas.create_text(150, 25, text='')
minbar = canvas.create_rectangle(0, 50, 0, 100, fill="blue")
mintxt = canvas.create_text(150, 75, text='')
hourbar = canvas.create_rectangle(0, 100, 0, 150, fill="magenta")
hourtxt = canvas.create_text(150, 125, text='')
daybar = canvas.create_rectangle(0, 150, 0, 200, fill="red")
daytxt = canvas.create_text(150, 175, text='')
mthbar = canvas.create_rectangle(0, 200, 0, 250, fill="yellow")
mthtxt = canvas.create_text(150, 225, text='')
yearbar = canvas.create_rectangle(0, 250, 0, 300, fill="green")
yeartxt = canvas.create_text(150, 275, text='')

edit()
root.mainloop()
