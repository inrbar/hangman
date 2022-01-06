import matplotlib.pyplot as plt
import matplotlib.animation as ani
import re
import calculations as c
import start as s
from tkinter import *

# To do:
#  - textbox in initial window to inform about problems
#  - maybe check why there are two plots
#  - readme update

window = Tk()
window.geometry('600x400')
window.title("Game of life configuration")
src_var = StringVar()

def submit():
    
    global src
    src = src_var.get()
    src = src.split(',')
    if len(src) == 1:
        src = str(src)
        src = re.sub(r'\W+', '', src)
    elif len(src) == 2:
        pass
    else:
        pass
    window.destroy()
     

src_txt = Label(window, text="If you'd like to load text file as source, input it's name in this box\nOr if you'd prefer creating random board, input it's size like this [x,y]", fg='black', font='none 12 bold')
src_box = Entry(window, width=20, textvariable=src_var, font='none 12 bold')

src_btn = Button(window,text = 'Submit', command = submit)

src_txt.grid(row=0, column=0)
src_box.grid(row=1,column=0)
src_btn.grid(row=1,column=1)

window.mainloop()



fig, ax = plt.subplots()

def update(i):
    global board
    board = c.logic(board)
    img.set_array(board)
    return img

if isinstance(src, str) :
    board = s.create_board_predef(src)
else:
    board = s.create_board_random(src)


img = ax.imshow(board)
animatio = ani.FuncAnimation(fig, update, interval=150, frames=30, blit=False)
plt.show()