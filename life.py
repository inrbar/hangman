import matplotlib.pyplot as plt
import matplotlib.animation as ani
import os
import calculations as c
import start as s
from tkinter import *

# To do:
#  - readme update

# creating window
window = Tk()
window.geometry('600x400')
window.title("Game of life configuration")
window.configure(background='gray')
src_var = StringVar()

# function determines which type of board creation method to choose
def submit():
    problem_box.delete(0.0, END)
    global src
    src = src_var.get()
    src = src.strip("[").strip(']')

    if "," in src:
        src = src.split(',')

        if len(src) == 2:
            window.destroy()
        else:
            mes = 'It seems you used too much commas, try again'
            problem_box.insert(END, mes)

    else:
        if os.path.isfile(f'sample_patterns/{src}.txt'):
            window.destroy()
        else:
            mes = "There's no such file in folder!"
            problem_box.insert(END, mes)
        pass

# setting up every
src_txt = Label(window, text="If you'd like to load text file as source, input it's name in this box\nOr if you'd prefer creating random board, input it's size like this [x,y]",bg='gray', fg='black', font='none 12 bold')
src_box = Entry(window, width=20, textvariable=src_var, bg='gray', font='none 12 bold')

src_btn = Button(window,text = 'Submit', command = submit)

problem_txt = Label(window, text='In case of any problems with your input, they will be displayed here', bg='gray', fg='black', font='none 10 normal')
problem_box = Text(window, width=25, height=4, bg='gray', wrap=WORD)

# postioning everything
src_txt.grid(row=0, column=0)
src_box.grid(row=1,column=0)
src_btn.grid(row=1,column=1)
problem_txt.grid(row=2, column=0)
problem_box.grid(row=3, column=0)

window.mainloop()

fig = plt.figure(facecolor='gray')
ax = plt.axes()

def update(i):
    global board
    board = c.logic(board)
    img.set_array(board)
    return img

# checking which creation method to use
if isinstance(src, str) :
    board = s.create_board_predef(src)
else:
    board = s.create_board_random(src)

fig = plt.gcf()
fig.canvas.manager.set_window_title('Game of life')

img = ax.imshow(board, aspect='equal', cmap='inferno')
animatio = ani.FuncAnimation(fig, update, interval=150, frames=30, blit=False)
plt.show()