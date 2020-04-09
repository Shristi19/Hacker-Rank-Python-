def swap_case(s):
    sa=[]
    for char in s:
        if char.isalpha():
            if char.isupper():
                sa.append(char.lower())
            else:
                sa.append(char.upper())
        else:
            sa.append(char)

    return ''.join(sa)




if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
