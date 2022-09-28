import sys
from collections import deque
sys.stdin = open('5521input.txt')

def bfs(N):
    q = deque([1])
    visited[1] = 1
    cnt = 0
    while q:
        s = q.popleft()
        cnt += 1
        if visited[s] <= 2:
            for i in range(1, N+1):
                if adj_M[s][i] and not visited[i]:
                    q.append(i)
                    visited[i] = visited[s] + 1
    return cnt-1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_M = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj_M[a][b] = 1
        adj_M[b][a] = 1
    # print(adj_M)

    visited = [0] * (N+1)
    print(f'#{tc} {bfs(N)}')
