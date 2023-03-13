#Write a Python function to calculate the factorial of a number (anonnegative integer)
def fact (num):
    fact =1
    if num <0:
        print("sorry ,factorial does not exit for negative integer")
    elif num == 0:
        print("please enter gerater number ")
    else:
        for i in range(1,num+1):
            fact = fact * i
        print("the factorial of ",num,"is : ",fact)

num1=int(input("enter number : "))
fact(num1)
