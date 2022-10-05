import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(n):
    res = []
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        s = q.popleft()
        for ns in [s-1, s+1, s*2]:
            if 0 <= ns < 100001:
                if visited[ns] == visited[s] + 1:
                    q.append(ns)
                elif visited[ns] == 0:
                    visited[ns] = visited[s] + 1
                    q.append(ns)
                if ns == K:
                    res.append(visited[ns])
                    visited[ns] = 0
                    q.pop()
    return res

N, K = map(int, sys.stdin.readline().split())
visited = [0] * 100001
if N < K:
    ans = bfs(N)
    x = min(ans)
    print(x)
    print(ans.count(x))
else:
    print(N-K)
    print(1)
