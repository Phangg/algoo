import sys
from collections import deque
sys.stdin = open('3input.txt')

#    우  하  좌  상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(x, y, arr):
    q = deque([[x, y]])                                                     # 큐에 x,y 출발점 넣고 시작
    arr[x][y] = 2                                                           # 방문 처리 2로 진행
    while q:
        x, y = q.popleft()                                                  # 큐에서 뽑은 곳을 출발점으로 설정 후 델타탐색
        for d in range(4):
            nx, ny = x + di[d], y + dj[d]
            if (0 <= nx < N) and (0 <= ny < M) and arr[nx][ny] == 0:
                q.append([nx, ny])                                          # 범위 내애서 가려는 곳이 0 일때 큐에 추가
                arr[nx][ny] = 2                                             # 방문 처리
    return 1                                                                # 탐색 완료 시, 1 반환

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# print(N, M)
# print(arr)

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt += bfs(i, j, arr)                                           # 탐색이 한번 잘 끝나면 +1
print(cnt)



# def dfs(x, y):
#     if (x < 0) or (y < 0) or (x >= N) or (y >= M):
#         return 0
#     elif arr[x][y] == 0:
#         arr[x][y] = 2
#         dfs(x, y+1)  # 우 하 좌 상 - 순서
#         dfs(x+1, y)
#         dfs(x, y-1)
#         dfs(x-1, y)
#         return 1
#     return 0
#
# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
#
# res = 0
# for i in range(M):
#     for j in range(N):
#         res += dfs(i, j)
# print(res)
