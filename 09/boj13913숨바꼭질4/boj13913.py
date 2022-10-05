import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = [0, 0]
    while q:
        s = q.popleft()
        for ns in [s-1, s+1, s*2]:
            if 0 <= ns < 100001 and not visited[ns]:
                q.append(ns)
                visited[ns] = [visited[s][0] + 1, s]
                if ns == K:
                    x = visited[ns]
    return x

N, K = map(int, sys.stdin.readline().split())
visited = [[] for _ in range(100001)]

if N < K:
    ans = bfs(N)
    print(ans[0])
    ans_lst = [K]
    a = ans[1]
    while a:
        ans_lst.append(a)
        a = visited[a][1]
    if N == 0:
        ans_lst.append(0)
    print(*ans_lst[::-1])

else:
    print(N-K)
    while N != K:
        print(N, end=' ')
        N -= 1
    print(K)
