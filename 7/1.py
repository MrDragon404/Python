import tkinter
from tkinter import colorchooser, HORIZONTAL

window = tkinter.Tk()
window.title("Paint on Python")

brush_size = 3
brush_color = "black"

def button_color_handler():
    global brush_color
    brush_color = colorchooser.askcolor()[1]


def button_size_handler():
    global brush_size
    brush_size = button_scale.get()

def button_clear_hander():
    canvas.delete("all")

def draw(event):
    global brush_size
    global brush_color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    canvas.create_oval(x2, y2, x1, y1, fill=brush_color, outline=brush_color)



canvas = tkinter.Canvas(window,
                        width=800,
                        height=600,
                        bg="white")

canvas.grid(row=2, column=0, columnspan=7)
canvas.bind("<B1-Motion>", draw)

button_color = tkinter.Button(window,
                              text="Color",
                              font=("Arial", 18),
                              command=button_color_handler
                              )
button_scale = tkinter.Scale(window,
                             from_=0,
                             to=70,
                             orient=HORIZONTAL
                             )

button_size = tkinter.Button(window,
                             text="Size",
                             bg="silver",
                             fg="black",
                             font=("Arial", 18),
                             command=button_size_handler
                             )

button_delete = tkinter.Button(window,
                               text="Clear",
                               bg="red",
                               fg="white",
                               font=("Arial", 18),
                               command=button_clear_hander
                               )
button_color.grid(row=0, column=1)
button_size.grid(row=0, column=2)
button_delete.grid(row=0, column=3)
button_scale.grid(row=0, column=4)







tkinter.mainloop()
