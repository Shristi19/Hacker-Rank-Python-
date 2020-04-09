def merge_the_tools(string, k):
    # your code goes here
    print(len(string))
    t = len(string)// k
    print(t)
    for i in range(0,len(string),k):
        an =[]
        x = string[i : i+k]
        print(x)
        y = [an.append(j) for j in x if j not in an]
        print(''.join(an))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
