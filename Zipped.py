# The first line contains and separated by a space.
# The next
#
# lines contains the space separated marks obtained by students in a particular subject.
#
# Constraints
#
#
# Output Format
#
# Print the averages of all students on separate lines.
#
# The averages must be correct up to
#
# decimal place.
#
# Sample Input

n, m = input().split()
n , m= int(n) , int(m)
li = []
for i in range(m):
    z = list(map(float, input().split()))
    li = li+[z]

y = list(zip(*li))

for i in y :
    v = sum(i)
    print("%0.1f"% (v / m))


