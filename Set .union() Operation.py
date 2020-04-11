
n = int(input())
set_n = set(map(int, input().split()))
m = int(input())
set_m = set(map(int, input().split()))
x = len(set_n.union(set_m))
print(x)
