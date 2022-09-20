import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs():
    global q
    while q:
        k, x, y = q.popleft()
        for dk, dx, dy in [[0, 0, 1], [0, 1, 0], [0, 0, -1], [0, -1, 0], [-1, 0, 0], [1, 0, 0]]:
            nk, nx, ny = k + dk, x + dx, y + dy
            if (0 <= nx < N) and (0 <= ny < M) and (0 <= nk < H) and (tmt[nk][nx][ny] == 0) and (visited[nk][nx][ny] == 0):
                tmt[nk][nx][ny] = tmt[k][x][y] + 1
                visited[nk][nx][ny] = 1
                q.append([nk, nx, ny])


M, N, H = map(int, sys.stdin.readline().split())
tmt = []
for _ in range(H):
    box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    tmt.append(box)
# print(tmt)

q = deque()
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
# print(visited)

zero = 0
one = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tmt[h][i][j] == 1:
                visited[h][i][j] = 1
                one += 1
                q.append([h, i, j])
            if tmt[h][i][j] == 0:
                zero += 1

if zero:
    bfs()
    print(tmt)
    # print(visited)
    fail = 0
    for b in tmt:
        for lst in b:
            if 0 in lst:
                fail = 1
                break
        if fail:
            break
    if fail:
        print(-1)
    else:
        print(max([max(map(max, ans)) for ans in tmt])-1)
else:
    if one:
        print(0)
    else:
        print(-1)