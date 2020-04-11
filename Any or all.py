# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

arr = list(map(int, input().split()))
y= []
x = []
[x.append('True') if i > 0 else x.append('False') for i in arr]
arr = list(map(str,arr))

[y.append('True') if i == i[::-1] else y.append('False') for i in arr]
print(x , y , end='\n')
if 'False' in x or  'True' not in y :
    print('False')
else:
    print('True')
