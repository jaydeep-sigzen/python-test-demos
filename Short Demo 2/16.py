#Write a Python program to check whether a list contains a sub list.
list = ['a','b','c',[50,'vishal']]
for i in list:

    if len(i) > 1:
        print("sublist is present in list")
        break
else:
     print("sublist is not present")
