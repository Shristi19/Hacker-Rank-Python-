# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
s= 'ab##'
t = 'c#d#'
n=len(s)
m= len(t)
i=0


def change( st ):
    i = 0
    s_new=[]
    while i < len(st):

        if st[i] == '#':
            s_new = s_new[:len(s_new) - 1]
        else:
            s_new.append(st[i])

        i += 1

    return s_new


s = change(s)

t = change(t)


s = [i for i in s if i != 4 and i != '#']
t = [i for i in t if i != 4 and i != '#']

s, t = ''.join(s), ''.join(t)
if s == t:
    print(True)
else:
    print(False)


