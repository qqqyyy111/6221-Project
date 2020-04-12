from tkinter import *
import tkinter as tk
from run import find_locate3d

root = Tk()


w = Canvas(
    root,
    root.title("WIFI Positioning"),
    width=400,
    height=400,
    background="white"
)
w.pack()

for i in range(0, 400, 20):
    w.create_line(0, i, 400, i, fill='gray', dash=(3, 5))
    w.create_line(i, 0, i, 400, fill='gray', dash=(3, 5))

def onclick(event):
    print("You clicked the button")

def locate():
    location_list = find_locate3d()
    xc = location_list[0]
    yc = location_list[1]
    print(xc, yc)

    x1, y1 = (xc * 40 - 3), (yc * 40 - 3)
    x2, y2 = (xc * 40 + 3), (yc * 40 + 3)
    w.create_oval(x1, y1, x2, y2, fill='yellow')

def update():
    w.delete(ALL)
    root.update()
    for i in range(0, 400, 20):
        w.create_line(0, i, 400, i, fill='gray', dash=(3, 5))
        w.create_line(i, 0, i, 400, fill='gray', dash=(3, 5))



B = tk.Button(text="locate!", command = locate)
B.pack()


mainloop()
