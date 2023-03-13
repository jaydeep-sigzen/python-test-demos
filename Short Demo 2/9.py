#Write a Python function that takes two lists and returns true if they haveat least one common member. 

list1=[5,6,7,8,9]
list2=[6,3,1,3,5]

for x in list1:
    for y in list2:
        if x==y:
            print("true")
