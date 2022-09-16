import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')

def bfs():
    q = deque()

    for i in range(N):
        for j in range(M):              # 시작점 2개인 경우 있음 / 함수 내에서 탐색 / q 에 append 하기
            if arr[i][j] == 1:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < N) and (0 <= ny < M) and (arr[nx][ny] == 0):
                arr[nx][ny] = arr[x][y] + 1
                q.append([nx, ny])


M, N = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(arr)

bfs()                                   # bfs 돌기

cnt = 0
for i in range(N):
    for j in range(M):                  # bfs 했는데, 0 이 있는지 체크
        if arr[i][j] == 0:
            cnt += 1

# pprint(arr)

if cnt == 0:
    print(max(map(max, arr))-1)         # 2차원 배열에서 가장 큰 값을 뽑는 방법 => max(map(max, {  }))
else:                                   # 시작점이 1이라 -1 해서 출력
    print(-1)                           # 0 이 있을 경우 => 토마토 다 익지 못하는 경우