string = 'aba'
y=[]
for x in string:
    if x not in y:
        y.append(x)

print(y)
