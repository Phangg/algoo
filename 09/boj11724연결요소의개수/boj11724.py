import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(s):
    global cnt
    q = deque()
    q.append(s)
    visited.add(s)
    while q:
        s = q.popleft()
        for j in graph[s]:
            if j not in visited:
                q.append(j)
                visited.add(j)
    cnt += 1


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)
cnt = 0
visited = set()
for i in range(1, N + 1):
    if i not in visited:
        bfs(i)
print(cnt)