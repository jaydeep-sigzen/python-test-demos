#Write a Python function that takes a list and returns a new list with unique elements of the first list.

list=[10,2,6,8,9,2,3,5,6,10]
unique_list=[]
for a in list:
    if a not in unique_list:
        unique_list.append(a)
print("new list : ",unique_list)


    
