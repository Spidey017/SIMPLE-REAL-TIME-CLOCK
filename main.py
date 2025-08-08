from tkinter import *
from time import strftime
import itertools

root = Tk()
root.title("Fabulous Digital Clock")
root.geometry("700x300")
root.resizable(False, False)

canvas = Canvas(root, width=700, height=300, highlightthickness=0)
canvas.pack(fill="both", expand=True)

colors = itertools.cycle([
    "#1e1e2f", "#282a36", "#3d3f58", "#44475a",
    "#6272a4", "#8be9fd", "#50fa7b", "#ffb86c", "#ff79c6"
])

def animate_bg():
    canvas.config(bg=next(colors))
    root.after(1000, animate_bg)

def update_time():
    label.config(text=strftime('%I:%M:%S %p'))
    root.after(1000, update_time)

label = Label(canvas, font=('Segoe UI', 60, 'bold'),
              bg='#1e1e2f', fg='cyan')
label.place(relx=0.5, rely=0.5, anchor=CENTER)

animate_bg()
update_time()
root.mainloop()
