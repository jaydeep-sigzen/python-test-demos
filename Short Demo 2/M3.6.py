#Write a Python program to count the number of strings where the string
#length is 2 or more and the first and last character are same from a given
#list of strings.
words=['abc', 'zyz', 'aba', '1221',]
ctr=0
for word in words:
    if len(word)>1 and word[0]==word[-1]:
      ctr += 1
print(ctr)
