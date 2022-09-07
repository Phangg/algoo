from pprint import pprint
import sys
sys.stdin = open('input.txt')

# node : 점 / edge :선
num_node, num_edge = map(int,input().split())

lst = [[] for _ in range(num_node)]

for _ in range(num_edge):
    s, e = map(int,input().split())
    lst[s].append(e)
    lst[e].append(s)
for idx, value in enumerate(lst):
    print(idx , ' : ', value)

# pprint(lst)

stack = []
# 0 : 방문 안한 것  / 1 : 방문 한 것
visited = [0] * num_node

# 시작점 : 0
s = 0
stack.append(s)
visited[s] = 1

while stack:
    value = stack[-1]
    visited[value] = 1
    for node in lst[value]:
        if visited[node] == 0:
            stack.append(node)
            break
    else:
        stack.pop()

# while stack:
#     value = stack[-1]
#     for node in lst[value]:
#         if visited[node] == 0:
#             stack.append(node)
#             visited[node] = 1
#             break
#     else:
#         stack.pop()










# print('--------------------------------------------------')

visited = [0]*num_node

def func(value):
    visited[value] = 1
    # 동작을 하시면 됩니다.
    for node in lst[value]:
        if visited[node] == 0:
            func(node)
    return None
func(0)










