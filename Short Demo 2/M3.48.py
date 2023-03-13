#Write a Python function to check whether a number is in a given range
def checkrange(n):
    if n in range(1,60):
        print("%s is in the range"%str(n))
    else:
        print("%s the number is not range"%str(n))
checkrange(15)
checkrange(28)
checkrange(66)
