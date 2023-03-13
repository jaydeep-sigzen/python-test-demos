#Write a Python program to find the repeated items of a tuple.

tup=(1,3,4,32,1,1,1,31,32,12,21,2,3)  
for i in tup:
    if tup.count(i) > 1:
        print("repeated items list : ",i)


print("*"*30)

var=int(input('find number : '))
tup=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
a=list(tup)
for i in range(len(a)):
  a[i]=int(a[i])
count=a.count(var)
print(var,'appears',count,'times in the tuple')
