from  itertools import combinations

N=4
string ='a a c d'
k= 2
string = list(string.replace(' ',''))

list_combo = list(combinations(string,k))
count = 0
for i in list_combo:
    if 'a' in i:
        count += 1

print(count / len(list_combo))

