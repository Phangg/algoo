import sys
from collections import deque
sys.stdin = open('input.txt')

# 지나간 곳을 0으로 바꿔버리고, 주변 델타 탐색해서 위력 체크
def bfs(si, sj, color):
    q = deque()
    q.append([si, sj])
    arr[si][sj] = 0
    res = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < M) and (0 <= ny < N) and arr[nx][ny] == color:
                arr[nx][ny] = 0
                q.append([nx, ny])
                res += 1
    return res**2


# input
N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(M)]

# B, W 위력을 카운팅할 변수 만들고, 배열 순회하면서 'B', 'W' 체크해서 bfs 함수 진입
B, W = 0, 0
for i in range(M):
    for j in range(N):
        if arr[i][j] == 'B':
            B += bfs(i, j, 'B')
        elif arr[i][j] == 'W':
            W += bfs(i, j, 'W')
print(W, B)