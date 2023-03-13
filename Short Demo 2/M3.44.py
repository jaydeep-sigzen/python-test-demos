#Write a Python program to find the highest 3 values in a dictionary

from collections import Counter
my_dict = {'A':99,'B':23,'C':101,'D':56,'E':12,'F':255}

k = Counter(my_dict)
high = k.most_common(3)

print("Dictionary:")
print(my_dict, "\n")
print("Dictionary with 3 highest values:")
print("Keys: Values")

for i in high:
	print(i[0]," : ",i[1]," ")



