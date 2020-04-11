# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5
#
# Sample Output
#
# 4


m = input()

x = set(map(int,input().split()))

n= int(input())


for i in range(n):
    y = input().split()
    if y[0] == "remove":
        x.remove(int(y[1]))
    elif y[0] == "pop":
        x.pop()
    elif y[0] == 'discard':
        x.discard(int(y[1]))

print(sum(x))
