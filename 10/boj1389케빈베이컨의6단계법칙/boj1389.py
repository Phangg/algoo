import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(start):
    q = deque()
    q.append(start)
    cnt = [0] * (N+1)
    visited = [0] * (N+1)
    while q:
        s = q.popleft()
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt[i] = cnt[s] + 1
    return sum(cnt) - cnt[start]


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

res = []
for i in range(N+1):
    res.append(bfs(i))
# print(res)

print(res.index(min(res[1:])))