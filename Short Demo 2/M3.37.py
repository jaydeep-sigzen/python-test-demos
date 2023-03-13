#Write a Python program to check multiple keys exists in a dictionary
dict={1:"sagar",2:"vishal",3:"vijay",4:"pankaj",5:"nisha",6:"kishor",7:"Dharti"}
keys={1,3,5}
if dict.keys() >= keys:
    print("All keys are present")
else:
    print("All keys are not present")

print("*"*30)

keys={6,3,9,10}
if dict.keys() >= keys:
    print("All keys are present")
else:
    print("All keys are not present")