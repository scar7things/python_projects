import tkinter as tk
from datetime import datetime

counter = 0  # Start from 00:00:00
running = False

def counter_label(label):
    def count():
        global counter
        if running:
            tt = datetime.fromtimestamp(counter)
            string = tt.strftime("%H:%M:%S")
            label['text'] = string

            # Update the label after 1000ms (1 second)
            label.after(1000, count)
            counter += 1

    count()  # Start the counter initially

def start(label):
    global running
    running = True
    counter_label(label)
    start_button['state'] = 'disabled'
    stop_button['state'] = 'normal'
    reset_button['state'] = 'normal'

def stop():
    global running
    start_button['state'] = 'normal'
    stop_button['state'] = 'disabled'
    reset_button['state'] = 'normal'
    running = False

def reset(label):
    global counter
    counter = 0  # Reset to 00:00:00

    if not running:
        reset_button['state'] = 'disabled'
        label['text'] = 'Welcome!'
    else:
        label['text'] = 'Starting...'

root = tk.Tk()
root.title("Stopwatch")
root.minsize(width=250, height=70)

label = tk.Label(root, text="Welcome", fg="black", font="verdana 30 bold")
label.pack()

f = tk.Frame(root)
start_button = tk.Button(f, text='Start', width=6, command=lambda: start(label))
stop_button = tk.Button(f, text='Stop', width=6, state='disabled', command=stop)
reset_button = tk.Button(f, text='Reset', width=6, state='disabled', command=lambda: reset(label))

f.pack(anchor='center', pady=5)
start_button.pack(side="left")
stop_button.pack(side="left")
reset_button.pack(side="left")

root.mainloop()

