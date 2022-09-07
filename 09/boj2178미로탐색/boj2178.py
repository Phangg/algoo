import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(x, y, ex, ey, arr):
    q = deque([[x, y]])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < N) and (0 <= ny < M) and (visited[nx][ny] == 0) and (arr[nx][ny] != 0):
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
            if (nx == ex) and (ny == ey):
                return visited[nx][ny]


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# print(arr)
i, j = 0, 0
ei, ej = N-1, M-1
visited = [[0]*M for _ in range(N)]

print(bfs(i, j, ei, ej, arr))