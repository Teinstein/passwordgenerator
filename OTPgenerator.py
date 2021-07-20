#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random as teinstein
from tkinter import *
from tkinter import messagebox

t=Tk()
var=StringVar()

def check():
        if(e2.get() == str(otp)):
             messagebox.showinfo("OTP verification","Login successful")
             print("Name:", e1.get())
             print("Gender : ",var.get())
             print("City :",e3.get())
             
        else:
             messagebox.showinfo("OTP verification","Login denied")
                          
            
def otpgenerator():
    global otp
    otp=""  
    for i in range(4):
        otp+=str(teinstein.randint(1,9))        
    print ("Your OTP is",otp)

        
label1= Label(t,text="Gender")                              
r1=Radiobutton(t,text="Male",variable= var,value="Male")
r2=Radiobutton(t,text="Female",variable= var,value="Female")
l1=Label(t,text="Name: ").pack()
e1=Entry(t)
e1.pack()
label1.pack()
r1.pack()
r2.pack()
l2=Label(t,text="Enter password:").pack()
e2=Entry(t)
e2.pack()
l3=Label(t,text="City : ").pack()
e3=Entry(t)
e3.pack()
b1=Button(t, text="Submit",command=check).pack()
b=Button(t, text="Generate otp",command=otpgenerator).pack()

t.mainloop()