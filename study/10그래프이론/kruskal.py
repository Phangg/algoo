'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''

def find_P(parent, x):
    if parent[x] != x:
        parent[x] = find_P(parent, parent[x])
    return parent[x]

def union_P(parent, a, b):
    a = find_P(parent, a)
    b = find_P(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [p for p in range(v+1)]

# 간선 오름차순으로 정렬
edge_lst = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edge_lst.append((cost, a, b))
edge_lst.sort()

# 간선 하나씩 체크
res = 0
for edge in edge_lst:
    cost, a, b = edge
    # 사이클 발생하지 않는 경우에만 union 진행 / 간선 가중치 값 res 에 더해주기
    if find_P(parent, a) != find_P(parent, b):
        union_P(parent, a, b)
        res += cost

print(res)