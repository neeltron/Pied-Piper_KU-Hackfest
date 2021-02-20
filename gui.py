from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import ImageTk, Image
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
import sklearn.metrics
from sklearn import datasets
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
import os



root = Tk()
root["bg"]="#121212"
root.title("AI Based Diagnosis App")

fontStyle = tkFont.Font(family="times new roman", size=15,weight="bold")
fontStyle_label = tkFont.Font(family="times new roman",size=12)

label0 = Label(root,text="Enter the following: ",font=fontStyle,anchor=W,fg="#cfe2f3",bg="#121212")
label0.grid(row=0,column=0,columnspan=5,sticky=W+E)


# Defining entries
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

# Creating labels and pushing entries
items=[("Age",e1),("Sex",e2),("Anaemia(1 - Yes | 0 - No)",e3),("Diabetes(1 - Yes | 0 - No)",e4),("High BP(1 - Yes | 0 - No)",e5),("Sex(2 - Other | 1 - Male | 0 - Female)",e6),("Smoker? (1 - Yes | 0 - No)",e7),("Time since last visit (days)",e8),("label9",e9),("label10",e10),("label11",e11),("label12",e12)]


for index,(lbl,e) in enumerate(items):
    Label(root,text=lbl,bg="#121212",fg="#cfe2f3",font=fontStyle_label).grid(row=index+1,column=0,pady=10,padx=(1,30))

    e.grid(row=index+1,column=1,columnspan=3,padx=2,pady=10)
    e["bg"]="#121212"
    e["fg"]="white"
    e["insertbackground"]="white"
    e["bd"]="2"

    
# Function to open another window 
def open():
  
    top=Toplevel()
    top["bg"]="#121212"
    top.title("Output")

    Label(top,text="Output: ",font=fontStyle,anchor=W,fg="#cfe2f3",bg="#121212").grid(row=0,column=0,columnspan=5,sticky=W+E)
    
    Label(top,text=("First"),borderwidth=2,relief="ridge",width=20,font=fontStyle_label,bg="#121212",fg="#cfe2f3").grid(row=1,column=0,columnspan=2,padx=(0,5),pady=5)
    Label(top,text=("Second"),borderwidth=2,relief="ridge",width=20,font=fontStyle_label,bg="#121212",fg="#cfe2f3").grid(row=1,column=3,columnspan=2,padx=(0,0))
    Label(top,text=("Third"),borderwidth=2,relief="ridge",width=20,font=fontStyle_label,bg="#121212",fg="#cfe2f3").grid(row=2,column=0,columnspan=2,padx=(0,5),pady=10)
    Label(top,text=("fourth"),borderwidth=2,relief="ridge",width=20,font=fontStyle_label,bg="#121212",fg="#cfe2f3").grid(row=2,column=3,columnspan=2,padx=(0,0))

    Button(top,text="Back",bg="#434343",fg="#cfe2f3",command=top.destroy).grid(row=3,column=0,columnspan=5,sticky=W+E)

# Functionn to clear the existing values
def clear():
    lst=[e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12]
    for e in lst:
        e.delete(0,END)

#Buttons
Button(root,text="Submit",command=open,relief="raised",bg="#434343",fg="#cfe2f3").grid(row=13,column=0,columnspan=4,sticky=W+E,pady=5)
Button(root,text="CLear All",command=clear,relief="raised",bg="#434343",fg="#cfe2f3").grid(row=14,column=0,columnspan=4,sticky=W+E)


root.mainloop()