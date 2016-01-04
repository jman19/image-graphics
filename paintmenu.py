from tkinter import *
from filters import *
from Cimpl import *

def set_image():
    filepath=choose_file()
    print(filepath)
    if filepath == "":
        print('y')
        image = load_image(choose_file())

window = Tk()
frame=Frame(window)
frame.pack()

frame2=Frame(window,borderwidth=4, relief=GROOVE)
frame2.pack(side='right')

load_image=Button(frame2,text='load image',command=set_image)
load_image.pack()
canvas_width = 600
canvas_height = 400
w = Canvas(window, 
           width=canvas_width,
           height=canvas_height)
w.pack(side='left')

y = int(canvas_height / 2)


    
mainloop()