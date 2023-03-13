import random
def random_line():
    lines = open(M3.5.txt).read().splitlines()
    return random.choice(lines)
print(random_line('M3.5.txt'))
