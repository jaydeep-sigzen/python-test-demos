#Write a Python function to insert a string in the middle of a string.
def insert_string(str,word):
    return str[:6 ]+word+str[ 6:]
print(insert_string("how you?"," you"))
