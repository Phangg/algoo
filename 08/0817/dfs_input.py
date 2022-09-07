from pprint import pprint
import sys
sys.stdin = open('input.txt')

# node : 점 / edge :선
num_node, num_edge = map(int,input().split())

#####################################################################################
# 첫번째
# lst = [[0]*num_node for _ in range(num_node)]
#
# for _ in range(num_edge):
#     s, e = map(int,input().split())
#     lst[s][e] = 1
#     lst[e][s] = 1
#
# pprint(lst)
#
# # 3 과 연결된 node 찾기
# for i in range(num_node):
#     if lst[3][i]:
#         print(i)


#####################################################################################

# 두번째

lst = [[] for _ in range(num_node)]

for _ in range(num_edge):
    s, e = map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)
for idx, value in enumerate(lst):
    print(idx , ' : ', value)

# 3 과 연결된 node 찾기
for i in lst[3]:
    print(i)

#####################################################################################
# # 세번째
# dic = dict()
# # for idx in range(num_node):
# #     dic[idx] = []
# dic = { idx : [] for idx in range(num_node)}
#
# for _ in range(num_edge):
#     s, e = map(int,input().split())
#     dic[s].append(e)
#     dic[e].append(s)
# for key, value in dic.items():
#     print(key, ' : ', value)



#####################################################################################
# 네번째


# # dic = dict()
#
# for _ in range(num_edge):
#     s, e = map(int,input().split())
#
#     # 1
#     if dic.get(s):
#         dic[s].append(e)
#     else:
#         dic[s] = [e]
#
#     # if dic.get(s) is None:
#     #     dic[s] = []
#     # dic[s].append(e)
#
#     if dic.get(e):
#         dic[e].append(s)
#     else:
#         dic[e] = [s]


#####################################################################################
# # 다섯번째


# dic = dict()

# for _ in range(num_edge):
#     s, e = map(int,input().split())
#     dic[s] = dic.get(s, []) + [e]
#     dic[e] = dic.get(e, []) + [s]





#####################################################################################
# 여섯번째

# from collections import defaultdict
# dic_lst = defaultdict(list)
# # dic_lst = defaultdict(set)
#
# for _ in range(num_edge):
#     s, e = map(int,input().split())
#     dic_lst[s].append(e)
#     dic_lst[e].append(s)
#
#     # dic_lst[s].add(e)
#     # dic_lst[e].add(s)







