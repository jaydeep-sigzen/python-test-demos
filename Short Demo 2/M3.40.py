#Write a Python program to combine two dictionary adding values for comon kmeys.

d1 = {"a": 100, "b": 200, "c":300}
d2 = {"a": 300, "b": 200,"d":400}
d3=d1.copy()
d3.update(d2)
for keys in d1:
    if keys in d2:
        d3[keys]=d1[keys]+d2[keys]
print(d3)


