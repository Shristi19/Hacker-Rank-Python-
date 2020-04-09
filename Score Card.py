# from itertools import combinations
#
# s , k = input().split()
# k = int(k)
# s = sorted(s)
# for i in range(1,k+1):
#     solution = list(combinations(s,i))
#     for j in solution:
#         k = ''.join(j)
#         print(k)
#
# #
#
# a = [6,3,1,4,5]
#
# a.sort()
# print(a)
if __name__ == '__main__':
    list_names_scores =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_names_scores.append([name ,score])
    list_names_scores.sort(key = lambda x: x[1])
    score = [i[1] for i in list_names_scores]
    set_score = set(score)
    max_1 = min(set_score)
    set_score.discard(max_1)
    second_max = min(set_score)



    for i in list_names_scores:
        if i[1] == second_max:
            print(i[0])
