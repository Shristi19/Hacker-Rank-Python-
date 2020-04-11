# Your task is to sort the string
#
# in the following manner:
#
#     All sorted lowercase letters are ahead of uppercase letters.
#     All sorted uppercase letters are ahead of digits.
#     All sorted odd digits are ahead of sorted even digits.

s = input()
lower , upper , odd, even = [], [], [],[]

for i in s:
    if i.isdigit():
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    elif i.isupper():
        upper.append(i)
    else:
        lower.append(i)
lower.sort()
upper.sort()
odd.sort()
even.sort()
print(''.join(lower),''.join(upper),''.join(odd),''.join(even),sep='')


# input : Sorting1234
# o/p : ginortS1324
