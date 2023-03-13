#Write a Python function that takes a list of words and returns the length of the longest one
a=['hardik','pankaj','narendra']
max=len(a)
longest=a[0]
for i in a:
    if(len(i)>max):
       max1=len(i)
       longest=i
print("The word with the longest length is:",longest)
