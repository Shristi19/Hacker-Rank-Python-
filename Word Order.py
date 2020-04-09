# 4
# bcdef
# abcdefg
# bcde
# bcdef
#
# Sample Output
#
# 3
# 2 1 1
n = int(input())
arr=[]
for i in range(n):
    arr.append(input())
di ={}

for i in range(n):
    if arr[i] in di:
        di[arr[i]] +=1
        arr[i]=0
    else:
        di[arr[i]] = 1

print(len(di))
for i in arr:
    if i != 0:
        print(di[i],end=' ')

