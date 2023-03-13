#Write a Python program to read a random line from a file.
import random

file=open("vishal.txt","r")
a=(file.read()).split(".")[:-1]
print(random.choice(a))