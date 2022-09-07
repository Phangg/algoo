import sys
sys.stdin = open('input.txt')

def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1                                   # 시작점 방문 표시
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:                             # 도착지인가
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:      # 델타 탐색 (우 하 좌 상)
            ni, nj = (i + di), (j + dj)
            # maze 범위 안에 있고, 벽이 아니고( != 1), 왔던 길이 아니라면
            if (0 <= ni < N) and (0 <= nj < N) and (maze[ni][nj] != 1) and (visited[ni][nj] == 0):
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # print(maze)

    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    print(f'#{tc} {bfs(sti, stj, N)}')