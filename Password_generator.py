#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string
import sys


print('Hello, Welcome to Password generator!')

length = int(input('\nEnter the length of password: '))
if length<8:
    print("Weak password. Try again ! ")
    sys.exit()
else:
    pass
    
       
ch= int(input("Enter type of Password\n 1. Letters only\n 2. Capital and small letters\n 3.Capital and small letters "
              "and numbers\n 4.Capital and small letters and numbers and special characters\n"))

                      

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation


def Letters():
    all= lower
    temp = random.sample(all,length)
    password = "".join(temp)
    print("Password generated is " ,password)

def Capitalsmall():
       all= lower + upper
       temp = random.sample(all,length)
       password = "".join(temp)
       print("Password generated is " ,password)
       
def Capitalsmallnumbers():
       all= lower + upper + num
       temp = random.sample(all,length)
       password = "".join(temp)
       print("Password generated is " ,password)   

def Capitalsmallnumbersspecial():
        all= lower + upper + num + symbols
        temp = random.sample(all,length)
        password = "".join(temp)
        print("Password generated is " ,password)
               
if (ch==1):
    Letters()
        

if (ch==2):
    Capitalsmall()
            
        
if (ch==3):
    Capitalsmallnumbers()
     
  
if (ch==4):
    Capitalsmallnumbersspecial()
    
    
    



       
        

        

        

