import sys
from collections import deque
from pprint import pprint
sys.stdin = open('4input.txt')

def bfs(x, y, arr):
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 우 하 좌 상
            nx, ny = x+di, y+dj
            if (0 <= nx < N) and (0 <= ny < M) and (arr[nx][ny] == 1):
                arr[nx][ny] = arr[x][y] + 1                 # 이동 전의 위치 + 1 => 첫 시작 위치가 1이었으니!
                q.append([nx, ny])
    return arr[N-1][M-1]                                    # 도착 위치는 좌표상은  N-1, M-1


# 동빈이는 1,1 에 위치 / 출구는 N,M 에 위치
#       0,0         /     N-1,M-1
# N 행 / M 열 / 갈 수 있는 길 : 1
N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
# print(N, M)
# pprint(miro)

i, j = 0, 0
print(bfs(i, j, miro))
