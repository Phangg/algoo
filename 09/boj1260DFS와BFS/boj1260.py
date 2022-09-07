import sys
from collections import deque
sys.stdin = open('input.txt')

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)


def bfs(x, graph, visited):
    q = deque([x])
    visited[x] = 1
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


N, M, V = map(int, sys.stdin.readline().split())
# print(N, M, V)
graph = [[]*(N+1) for _ in range(N+1)]
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
for s, e in lst:
    graph[s].append(e)
    graph[e].append(s)
for r in range(1, N+1):
    graph[r].sort()                     # 여러개일때는 숫자 순서대로니까 소팅
print(graph)


visited = [0] * (N+1)                   # visited가 dfs / bfs 에서 둘 다 사용되니, 한번씩 만들기
dfs(graph, V, visited)
print()
visited = [0] * (N+1)
bfs(V, graph, visited)

