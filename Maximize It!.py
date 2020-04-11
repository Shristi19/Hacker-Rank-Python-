from itertools import product
k, m = input().split()
k, m = int(k) , int(m)
x=[]
for i in range(k):
    x.append(list(map(int, input().split())))
y= [ ]

x = list(map(lambda x : sum(i**2 for i in x)%m , product(*x)))
print(max(x))
