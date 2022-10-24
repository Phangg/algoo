import sys
import heapq
sys.stdin = open('input.txt')

# 사이클 확인
def find_p(x):
    if parent[x] != x:
        parent[x] = find_p(parent[x])
    return parent[x]


# v: 노드 개수 / e: 간선 개수
# a: 시작 노드 / b: 도착 노드 / c: 가중치
# edge_lst: heapq
v, e = map(int, sys.stdin.readline().split())
parent = [p for p in range(10000 + 1)]
edge_lst = []
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    # 가중치 먼저 넣기 (편한 정렬 위해서)
    heapq.heappush(edge_lst, (c, a, b))

# union 과정
res = 0
while edge_lst:
    c, a, b = heapq.heappop(edge_lst)
    find_p(a)
    find_p(b)
    pa, pb = parent[a], parent[b]
    if pa == pb:
        continue
    elif pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa
    res += c
print(res)