from tkinter import*

root = Tk()
root.geometry("400x355")

def hello():
    print("Hello Everyone")

def name():
    print("Name is Harry")


def submit():
    print("Done")

frame = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")

b1 = Button(frame,fg="red",text="Print now",command=hello)
b1.pack(side=LEFT,padx=20)

b2 = Button(frame,fg="red",text="Tell me name now",command=name)
b2.pack(side=LEFT,padx=20)

b3 = Button(frame,fg="red",text="submit now",command=submit)
b3.pack(side=LEFT,padx=20)

root.mainloop()