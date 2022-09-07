import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                            # N * N 배열 / M : 범위(?), 2 <= M <= N
    lst = [[0]*(N+(2*(M-1)))]*(M-1) + [[0]*(M-1) + list(map(int, input().split())) + [0]*(M-1) for _ in range(N)] + [[0]*(N+(2*(M-1)))]*(M-1)
    # pprint(lst)

    fly = 0
    for i in range(M-1, N+M-1):
        for j in range(M-1, N+M-1):
            garo_sero = 0
            garo_sero += lst[i][j]
            X = 1
            while X <= M - 1:
                #     우 상 좌 하
                di = [0, -X, 0, X]
                dj = [X, 0, -X, 0]
                for d in range(4):                                      # 십자가일 때
                    ni, nj = (i + di[d]), (j + dj[d])
                    garo_sero += lst[ni][nj]
                X += 1
            if fly < garo_sero:
                fly = garo_sero

    for i in range(M - 1, N+M-1):
        for j in range(M - 1, N+M-1):
            degak = 0
            degak += lst[i][j]
            X = 1
            while X <= M - 1:
                #  우상  좌상  좌하  우하
                dp = [-X, -X, X, X]
                dq = [X, -X, -X, X]
                for d in range(4):                                      # 대각선일 때
                    ni, nj = (i + dp[d]), (j+dq[d])
                    degak += lst[ni][nj]
                X += 1
            if fly < degak:
                fly = degak
    print(f'#{tc} {fly}')
