import numpy
n , m = input().split()
n , m = int(n) , int(m)
ans = []
for i in range(n):
    ans.append(list(map(int,input().split())))

ans = numpy.array(ans)

print(max(numpy.min(ans,axis = 1)))

########################################
import numpy
n , m = input().split()
n , m = int(n) , int(m)
ans = []
for i in range(n):
    ans.append(list(map(int,input().split())))

ans = numpy.array(ans)

print(numpy.mean(ans,axis = 1))
print(numpy.var(ans,axis = 0))
print('%0.11f'%numpy.std(ans,axis = None))

