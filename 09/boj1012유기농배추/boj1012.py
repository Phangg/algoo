import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')

def bfs(arr, si, sj):
    visited = [[0]*N for _ in range(M)]
    q = deque([[si, sj]])
    arr[si][sj] = 0
    visited[si][sj] = 1
    while q:
        si, sj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = si+di, sj+dj
            if (0 <= ni < M) and (0 <= nj < N) and (arr[ni][nj] == 1) and (visited[ni][nj] == 0):
                q.append([ni, nj])
                visited[ni][nj] = 1
                arr[ni][nj] = 0
    return 1                                                # 방문지역 체크하면서 탐색 다 돌면 1 반환

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    # print(M, N, K)
    farm = [[0]*N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        farm[x][y] = 1                                      # 배추가 있는 곳 표시
    # pprint(farm)

    ans = 0
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1:                             # 배추 발견시, bfs 함수 go!
                ans += bfs(farm, i, j)
    print(ans)