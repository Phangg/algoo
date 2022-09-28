import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(s):
    q = deque()
    q.append(s)
    while q:
        s = q.popleft()
        for ns in [s+1, s-1, s*2, s-10]:
            if 0 < ns < 1000001 and not visited[ns]:
                visited[ns] = visited[s] + 1
                if ns == M:
                    return visited[ns]
                else:
                    q.append(ns)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    print(f'#{tc} {bfs(N)}')
