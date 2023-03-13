#Write a Python program to map two lists into a dictionary
keys=[1,2,3,4,5]
values=["vishal","pankaj","komal","kishor","nisha"]
dict={}
for i in range(len(keys)):
    dict[values[i]]=keys[i]

print(dict)