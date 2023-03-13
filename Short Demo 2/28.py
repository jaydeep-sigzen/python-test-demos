#Write a Python program to remove an empty tuple(s) from a list of tuples.


list_tuples = [('one',),(),('two',),(),('three',)]

for item in list_tuples:
    if item==():
        list_tuples.remove(item)

print('new tuple list : ',list_tuples)  
