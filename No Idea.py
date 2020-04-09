
n , m = input().split()
n , m = int(n), int(m)

array = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

happy =0

for i in array:
    if i in a:
        happy += 1
    elif i in b:
        happy -= 1
print(happy)
