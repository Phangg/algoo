import sys
from collections import deque
sys.stdin = open('input.txt')

# 출발 지점 ~ 도착 지점 까지 지나간 칸의 개수 (출발지, 도착지 미 포함)

def bfs(sx, sy, ex, ey, arr):
    visited = [[0]*N for _ in range(N)]
    q = deque([(sx, sy)])
    visited[sx][sy] = 1
    while q:
        sx, sy = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = sx+dx, sy+dy
            if (0 <= nx < N) and (0 <= ny < N) and (arr[nx][ny] == 0) and (visited[nx][ny] == 0):
                q.append((nx, ny))
                visited[nx][ny] = visited[sx][sy] + 1
            elif nx == ex and ny == ey:                     # 도착 지점이 nx, ny 라면
                return visited[sx][sy] - 1                  # sx, sy 일때의 값 (출발지 포함 도착지 미 포함)에서 출발지 빼기 위해 -1 해주기
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    si = sj = ei = ej = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                si, sj = i, j                               # 출발 지점 (2) 좌표
            elif miro[i][j] == 3:
                ei, ej = i, j                               # 도착 지점 (3) 좌표

    print(f'#{tc} {bfs(si, sj, ei, ej, miro)}')