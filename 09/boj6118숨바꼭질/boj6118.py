import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        s = q.popleft()
        for i in farm[s]:
            if visited[i] == -1:
                visited[i] = visited[s] + 1
                q.append(i)


N, M = map(int, sys.stdin.readline().split())
farm = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    farm[a].append(b)
    farm[b].append(a)

visited = [-1] * (N + 1)
bfs(1)

ans = []
x = max(visited)
for idx, k in enumerate(visited):
    if k == x:
        ans.append(idx)
        ans.append(k)
        break
ans.append(visited.count(x))
print(*ans)