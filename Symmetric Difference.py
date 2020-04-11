m = int(input())
set_m = set(map(int, input().split()))
n = input()
set_n = set(map(int, input().split()))
x = list(set_m.difference(set_n))
y = list(set_n.difference(set_m))

z = x+y
z.sort()
print(*z, sep='\n')
