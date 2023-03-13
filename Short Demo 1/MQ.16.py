#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1=input("Enter First String : ")
str2=input("Enter Second String : ")
print('separated by sapace :',str1+'  '+str2)
x=str2[:2]+str1[2:]
y=str1[:2]+str2[2:]
print("swap first two char: ",x+' '+y)
