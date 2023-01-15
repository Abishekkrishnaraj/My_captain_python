# My_captain_python
# Online Python - IDE, Editor, Compiler, Interpreter

#1st task to find are of circle

import math

R=int(input("enter the radius of circle=")) 

A=math.pi*(R**2) 

print("Area of the circle =", A)

import pathlib 

  

#2nd task function to return the file extension 

x=input("file name")

file_extension = pathlib.Path(x).suffix 

print("File Extension: ", file_extension)
