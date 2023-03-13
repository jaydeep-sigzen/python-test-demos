#Write a Python function that checks whether a passed string is palindrome or not
def palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False
print(palindrome("vishal"))
print(palindrome("madam"))
