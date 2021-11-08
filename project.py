# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:25:27 2021

@author: stuti
"""

from tkinter import*

root=Tk()
root.title("Driving License")
root.geometry("300x400")
root.configure(bg="white")

label_name=Label(root)
label_grade=Label(root)
label_subjects= Label(root)

def myCard():
    name= "Maanya"
    print(type(name))
    pin_no= 451478
    print(type(pin_no))
    address=["Disney Land","Hong Kong"]
    print(type(address))
    
    label_name['text']=name
    label_grade['text']=pin_no
    label_subjects['text']=address
    
button1= Button(root,text="Show The Driving License",command=myCard)

label_name.place(relx=0.2,rely=0.3,anchor=W)
label_grade.place(relx=0.2,rely=0.4,anchor= W)
label_subjects.place(relx=0.2,rely=0.5,anchor=W)
button1.place(relx=0.2,rely=0.6,anchor=CENTER)

root.mainloop()