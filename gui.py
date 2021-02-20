from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import ImageTk, Image

root = Tk()
root["bg"]="#121212"
root.title("KU-Hackfest")
fontStyle = tkFont.Font(family="Lucida Grande", size=15)

label0 = Label(root,text="Enter parameters: ",font=fontStyle,anchor=W,fg="white",bg="#121212")
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
items=[(label1,e1),(label2,e2),(label3,e3),(label4,e4),(label5,e5),(label6,e6),(label7,e7),(label8,e8),(label9,e9),(label10,e10),(label11,e11),(label12,e12)]
for index,(lbl,e) in enumerate(items):
    lbl.grid(row=index+1,column=0,pady=10,padx=(1,30))
    lbl["bg"]="#121212"
    lbl["fg"]="white"

    e.grid(row=index+1,column=1,columnspan=3,padx=2,pady=10)
    e["bg"]="#121212"
    e["fg"]="white"
    e["insertbackground"]="white"

    
# Function to open another window 
def open():
    top=Toplevel()
    top["bg"]="#121212"
    top.title("analysis")
    
    Label(top,text=("First"),borderwidth=2,relief="ridge",width=20,bg="#121212",fg="white").grid(row=0,column=0,columnspan=2,padx=(0,5),pady=5)
    Label(top,text=("Second"),borderwidth=2,relief="ridge",width=20,bg="#121212",fg="white").grid(row=0,column=3,columnspan=2,padx=(0,0))
    Label(top,text=("Third"),borderwidth=2,relief="ridge",width=20,bg="#121212",fg="white").grid(row=1,column=0,columnspan=2,padx=(0,5),pady=10)
    Label(top,text=("fourth"),borderwidth=2,relief="ridge",width=20,bg="#121212",fg="white").grid(row=1,column=3,columnspan=2,padx=(0,0))

    Button(top,text="Back",bg="#121212",fg="white",command=top.destroy).grid(row=2,column=0,columnspan=5,sticky=W+E)
    top.pack()

# Functionn to clear the existing values
def clear():
    lst=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]
    for e in lst:
        e.delete(0,END)

#Buttons
Button(root,text="Submit",command=open,bg="#121212",fg="#cfe2f3").grid(row=13,column=0,columnspan=4,sticky=W+E,pady=5)
Button(root,text="CLear All",command=clear,bg="#121212",fg="#cfe2f3").grid(row=14,column=0,columnspan=4,sticky=W+E)


root.mainloop()