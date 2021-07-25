from tkinter import *

def drop_right():
    select = list(box_left.curselection())
    select.reverse()
    for i in select:
        box_right.insert(END, box_left.get(i))
        box_left.delete(i)

def drop_left():
    select = list(box_right.curselection())
    select.reverse()
    for i in select:
        box_left.insert(END, box_right.get(i))
        box_right.delete(i)



root = Tk()

box_left = Listbox(width=40, height=10, selectmode=EXTENDED)
box_right = Listbox(width=40, height=10, selectmode=EXTENDED)
f = Frame()
but1 = Button(f, text='>>>', command=drop_right)
but2 = Button(f, text='<<<', command=drop_left)

for i in ('one', 'two', 'three', 'im bored'):
    box_left.insert(END, i)


box_left.pack(side=LEFT)
f.pack(side=LEFT)
but1.pack(anchor=N)
but2.pack()
box_right.pack(side=LEFT)


root.mainloop()