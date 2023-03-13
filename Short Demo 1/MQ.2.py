#Write a Python program to get the Factorial number of given number.

n=int(input("Enter a number: "))
factorial=1
if n>1:
    for i in range(1,n+1):
        factorial=factorial*i
print("Factorail of ",n ," is :",factorial)
