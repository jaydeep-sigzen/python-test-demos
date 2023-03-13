#Write a Python program to get unique values from a list.

list=['java','python','c++','php','java','python','ruby']
l=[]
for x in list:
    if x not in l:
        l.append(x)
print("given list : ",list)
print("unique values : ",l)
