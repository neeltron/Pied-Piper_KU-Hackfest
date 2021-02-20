from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import ImageTk, Image

root = Tk()
root["bg"]="black"

fontStyle = tkFont.Font(family="Lucida Grande", size=15)

label0 = Label(root,text="Enter parameters: ",font=fontStyle,anchor=W,fg="white",bg="black")
label0.grid(row=0,column=0,columnspan=5,sticky=W+E)

"""
label1 = Label()
label2 = Label()
label3 = Label()
label4 = Label()
label5 = Label()
label6 = Label()
label7 = Label()
label8 = Label()
label9 = Label()
label10 = Label()
label11 = Label()
label12 = Label()

e1 = Entry()
e2 = Entry()
e3 = Entry()
e4 = Entry()
e5 = Entry()
e6 = Entry()
e7 = Entry()
e8 = Entry()
e9 = Entry()
e10 = Entry()
e11 = Entry()
e12 = Entry()
"""
# Defining labels and entries
label1 = Label(root,text="Label1")
e1 = Entry(root,bd=2)

label2 = Label(root,text="Label2")
e2 = Entry(root,bd=2)

label3 = Label(root,text="Label3")
e3 = Entry(root,bd=2)

label4 = Label(root,text="Label4")
e4 = Entry(root,bd=2)

label5 = Label(root,text="Label5")
e5 = Entry(root,bd=2)

label6 = Label(root,text="Label6")
e6 = Entry(root,bd=2)

label7 = Label(root,text="Label7")
e7 = Entry(root,bd=2)

label8 = Label(root,text="Label8")
e8 = Entry(root,bd=2)

label9 = Label(root,text="Label9")
e9 = Entry(root,bd=2)

label10 = Label(root,text="Label10")
e10 = Entry(root,bd=2)

label11 = Label(root,text="Label11")
e11 = Entry(root,bd=2)

label12 = Label(root,text="Label12")
e12 = Entry(root,bd=2)

# Pushing labels and entries
label=[label1,label2,label3,label4,label5,label6,label7,label8,label9,label10,label11,label12]
for index,lbl in enumerate(label):
    lbl.grid(row=index+1,column=0,pady=10)
    lbl["bg"]="black"
    lbl["fg"]="white"

lst=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]
for index,e in enumerate(lst):
    e.grid(row=index+1,column=1,columnspan=3,padx=10,pady=10)
    e["bg"]="black"
    e["fg"]="white"
    e["insertbackground"]="white"

# Function to open another window 
def open():
    top=Toplevel()
    top["bg"]="black"
    top.title("analysis")
    Label(top,text="Done",bg="black",fg="white").grid(row=0,column=0)
    Button(top,text="Exit",bg="black",fg="white",command=top.destroy).grid(row=1,column=0)

# Functionn to clear the existing values
def clear():
    lst=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]
    for e in lst:
        e.delete(0,END)

#Buttons
Button(root,text="Submit",command=open,bg="black",fg="white").grid(row=13,column=0,columnspan=5,sticky=W+E,pady=5)
Button(root,text="CLear All",command=clear,bg="black",fg="white").grid(row=14,column=0,columnspan=5,sticky=W+E)


root.mainloop()