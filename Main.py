#!/usr/bin/python3

import tkinter as tk
from tkinter import messagebox

###################################################
# from https://stackoverflow.com/questions/47996285/how-to-draw-a-line-following-your-mouse-coordinates-with-tkinter
###################################################
def draw(event):
    x, y = event.x, event.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)
    canvas.old_coords = x, y

def draw_line(event):

    if str(event.type) == 'ButtonPress':
        canvas.old_coords = event.x, event.y

    elif str(event.type) == 'ButtonRelease':
        x, y = event.x, event.y
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1)

def reset_coords(event):
    canvas.old_coords = None


root = tk.Tk()
root.title("billiard-tkinter")


canvas = tk.Canvas(root, width=500, height=500)



# draw a ball
bx1 = 10
bx2 = 16
by1 = 10
by2 = 16
ball = canvas.create_oval(bx1, by1, bx2, by2, fill='#000000')
canvas.pack()
canvas.old_coords = None

root.bind('<ButtonPress-1>', draw_line)
root.bind('<ButtonRelease-1>', draw_line)

root.mainloop()