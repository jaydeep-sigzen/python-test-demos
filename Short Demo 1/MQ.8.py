#Write a Python program to test whether a passed letter is a vowel or not.

x=input(" enter a word =")
for i in x:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        #print(i)
        print("vowel")
    else:
        print("not a vowel")
