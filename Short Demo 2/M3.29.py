#Write a Python program to unzip a list of tuples into individual lists. 

l = [(1,2), ("pankaj","vishal"),("vakhela","raval")]
print(list(zip(*l)))
