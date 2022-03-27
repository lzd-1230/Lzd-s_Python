
import sys
import os

if getattr(sys, 'frozen', False):
    pathname = sys._MEIPASS
else:
    pathname = os.path.split(os.path.realpath(__file__))[0]

filepath = "data.txt"
file_path = os.path.join(pathname,filepath) 
print(file_path)

with open(file_path,mode="r") as f:
    a,b = int(f.readline().strip("\n")),int(f.readline().strip("\n"))
    print(a+b)