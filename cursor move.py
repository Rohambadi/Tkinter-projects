from tkinter import *

window = Tk()


def myfunc(event):
    draw(event.x, event.y)

    
def draw(x, y):
    paint.coords(circle, x-20, y-20, x+20, y+20)

    
window.title("move with mouse")
paint = Canvas(window)
paint.bind('<Motion>', myfunc)
paint.pack()
circle = paint.create_oval(0, 0, 0, 0, fill="yellow")
window.mainloop()
