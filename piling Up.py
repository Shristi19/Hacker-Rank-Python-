test_cases = int(input())
x = []
for i in range(test_cases) :
    j = int(input())
    x.append(list(map(int, input().split())))

for i in x :
    y = []
     
    y.append(i[0],i[-1])
    j = 1
    k = -2
    while j <= k:

        j += 1
        k -= 1
