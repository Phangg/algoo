import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(n):
    visited = [-1] * 100001
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        s = q.popleft()
        for ns in [s-1, s+1, s*2]:
            if 0 <= ns < 100001 and visited[ns] == -1:
                if ns == (s*2):
                    visited[ns] = visited[s]
                    q.appendleft(ns)            # 곱하기만 계속 하는 경우가 있으니 q의 맨앞으로 보내주기..ㅠㅠ
                else:
                    visited[ns] = visited[s] + 1
                    q.append(ns)
            if ns == K:
                return visited[ns]

N, K = map(int, sys.stdin.readline().split())
if N < K:
    print(bfs(N))
else:
    print(N-K)