from tkinter import *

counter = -1
running = False


def counter_label(label):
    def count():
        if running:
            global counter
            if counter is -1:
                display = "Starting..."
            else:
                display = str(counter)
            label['text'] = display
            label.after(1000, count)
            counter += 1

    count()


def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


def Reset(label):
    global counter
    counter = -1
    if running is False:
        reset['state'] = 'disabled'
        label['text'] = 'Welcome'
    else:
        label['text'] = 'Starting...'


window = Tk()
window.title("StopWatch")
window.minsize(width=250, height=80)
window.resizable(False, False)

label = Label(window, text="Welcome", fg="purple", font="Tahoma 15 bold")
label.pack()

start = Button(window, text="Start", width=15, command=lambda: Start(label))
start.pack()

stop = Button(window, text="Stop", width=15, state='disabled', command=Stop)
stop.pack()

reset = Button(window, text="Reset", width=15, state='disabled', command=lambda: Reset(label))
reset.pack()

window.mainloop()
