# Write python program that swap two number with temp variable and without temp variable

x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))
temp=x
x=y
y=temp
print("after swapping x :",(x))
print("after swapping y :",(y))

#without temp variable
x=5
y=10
x,y=y,x
print("x =", x)
print("y =", y)


