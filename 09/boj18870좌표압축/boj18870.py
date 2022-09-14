import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
                                # [2, 4, -10, 4, -9]
st = sorted(list(set(lst)))
dic = {}                        # {-10: 0, -9: 0, 2: 0, 4: 0}

for i in range(len(st)):        # {-10: 0, -9: 1, 2: 2, 4: 3}
    dic[st[i]] = i
# print(dic)

for i in range(len(lst)):
    lst[i] = dic.get(lst[i])    # [2, 3, 0, 3, 1]
print(*lst)


# dic = {}
# for idx, s in enumerate(lst):
#     dic[s] = 0
#
# for i in lst:
#     cnt = 0
#     if dic[i] != 0:
#         cnt = dic[i]
#     else:
#         for j in dic.keys():
#             if i > j:
#                 cnt += 1
#     dic[i] = cnt
# for a in lst:
#     print(dic[a], end=' ')



# st = sorted(list(set(lst)))
# print(st)
#
# for a in lst:
#     print(st.index(a), end=' ')
