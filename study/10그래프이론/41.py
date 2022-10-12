import sys
sys.stdin = open('41input.txt')

def find_p(parent, x):
    if parent[x] != x:
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union_p(parent, a, b):
    a = find_p(parent, a)
    b = find_p(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
goal = list(map(int, sys.stdin.readline().split()))
parent = [p for p in range(N+1)]

# arr 순회 중 1 (이동 가능) 이면 union 해주기)
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            union_p(parent, i+1, j+1)
# print(parent)

# 루트가 같지 않으면 (사이클이 없다면) flag 를 0으로 바꾸기
flag = 1
for i in range(M-1):
    if find_p(parent, goal[i]) != find_p(parent, goal[i+1]):
        flag = 0

# flag == 1 -> 사이클이 있다면 'YES'
if flag:
    print('YES')
else:
    print('NO')