#Write a Python program to find the second smallest number in a list.
a=[]
num=int(input("enter a list size:"))
for i in range(num):
    val=int(input("enter number:"))
    a.append(val)

print("smallest number :",a[0])
print("second smallest number:",a[1])
