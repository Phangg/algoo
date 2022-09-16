import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    c = N//2
    arr[c-1][c-1] = arr[c][c] = 2
    arr[c-1][c] = arr[c][c-1] = 1
    # print(arr)

    b_cnt = 2       # 흑돌 카운트
    w_cnt = 2       # 백돌 카운트

    for _ in range(M):
        x, y, color = map(int, input().split())
        j, i = x-1, y-1
        arr[i][j] = color

        # 흑돌
        if color == 1:
            b_cnt += 1   #   우      하       좌       상       우상      우하      좌하      좌상
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]:
                if (0 <= i+dx < N) and (0 <= j+dy < N):
                    if arr[i+dx][j+dy] == 2:
                        for k in range(1, N):
                            if (0 <= i + dx*k < N) and (0 <= j + dy*k < N):
                                if arr[i + dx*k][j + dy*k] == 0:
                                    break
                                if arr[i + dx*k][j + dy*k] == 1:
                                    for t in range(1, k):
                                        arr[i + dx * t][j + dy * t] = 1
                                        b_cnt += 1
                                        w_cnt -= 1
                                    else:
                                        break

        # 백돌
        elif color == 2:
            w_cnt += 1   #   우      하       좌       상       우상      우하      좌하      좌상
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]:
                if (0 <= i+dx < N) and (0 <= j+dy < N):
                    if arr[i+dx][j+dy] == 1:
                        for k in range(1, N):
                            if (0 <= i + dx*k < N) and (0 <= j + dy*k < N):
                                if arr[i + dx*k][j + dy*k] == 0:
                                    break
                                if arr[i + dx*k][j + dy*k] == 2:
                                    for t in range(1, k):
                                        arr[i + dx * t][j + dy * t] = 2
                                        w_cnt += 1
                                        b_cnt -= 1
                                    else:
                                        break
    # pprint(arr)

    print(f'#{tc}', b_cnt, w_cnt)