from tkinter import *
import time

w = 800
h = 600


window = Tk()
window.title("Drawing and Move")
canvas = Canvas(window, width=w, height=h)
canvas.pack()

ball = canvas.create_oval(10, 10, 60, 60, fill="orange")

yspeed = 5
xspeed = 4


while True:
    canvas.move(ball, xspeed, yspeed)
    p = canvas.coords(ball)
    if p[3]>=h or p[1]<=0:
        yspeed = -yspeed
    if p[2]>=w or p[0]<=0:
        xspeed = -xspeed
    window.update()
    time.sleep(0.03)

window.mainloop()
