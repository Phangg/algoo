import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input.txt')

def bfs(x, y, ex, ey, arr):
    visited = [[0] * N for _ in range(N)]
    q = deque([[x, y]])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < N) and (0 <= ny < N) and (arr[nx][ny] == 0) and (visited[nx][ny] == 0):
                q.append([nx, ny])
                visited[nx][ny] = 1
            if nx == ex and ny == ey:
                return 1
    return 0



T = 10
N = 16
for _ in range(T):
    tc = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    # pprint(miro)

    x, y = 1, 1

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 3:
                ei, ej = i, j

    print(f'#{tc} {bfs(x, y, ei, ej, miro)}')