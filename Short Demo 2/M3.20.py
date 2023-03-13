#Write a Python program to create a tuple with numbers ex.fibonacci series.

a,b=0,1
tuple=()
for index in range(10):
    tuple +=(a,)
    a,b = b,a+b
print("fibonacci series stored in tuple : ",tuple)

