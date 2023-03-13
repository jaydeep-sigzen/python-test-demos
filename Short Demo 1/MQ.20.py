#Write a Python function to reverses a string if its length is a multiple of 4.
str="abcd"
str2="python"
def reverse_string(str):
    if len(str)%4==0:
       return''.join(reversed(str))
    return str
print(reverse_string(str))
print(reverse_string(str2))
