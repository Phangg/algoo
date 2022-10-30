import sys
from collections import deque
from copy import deepcopy
sys.stdin = open('16input.txt')

# 2(바이러스 시작지점)을 q 에 넣고, 넓이 우선 탐색을 통해, tmp_arr 를 바이러스가 갈 수 있는 만큼 물들이기
def bfs(tmp_arr):
    q = deque()
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < n) and (0 <= ny < m) and tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                q.append((nx, ny))

# bfs 완료 되면, 안전지역 체크
    safety = 0
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 0:
                safety += 1
    return safety


# 벽을 만드는 과정 / 재귀
def make_wall(cnt):
    global answer
    if cnt == 3:
        tmp_arr = deepcopy(arr)
        answer = max(answer, bfs(tmp_arr))
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
                make_wall(cnt)
                cnt -= 1
                arr[i][j] = 0


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


answer = 0
cnt = 0
make_wall(cnt)
print(answer)
