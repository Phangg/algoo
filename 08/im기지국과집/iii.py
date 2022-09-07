# A : 1칸 커버 기지국 / B : 2칸 커버 기지국 / C : 3칸 커버 기지국 / H : 집

import sys
from pprint import pprint
sys.stdin = open('input.txt')

#    우  하  좌  상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = 3
for tc in range(1, T+1):
    N = int(input())
    M = 10
    ss_map = [list(input()) for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if ss_map[i][j] == 'A':
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if (0 <= ni < N) and (0 <= nj < N) and (ss_map[ni][nj] == 'H'):
                        ss_map[ni][nj] = 'x'
            elif ss_map[i][j] == 'B':
                for k in range(1, 3):
                    for d in range(4):
                        ni = i + (di[d]*k)
                        nj = j + (dj[d]*k)
                        if (0 <= ni < N) and (0 <= nj < N) and (ss_map[ni][nj] == 'H'):
                            ss_map[ni][nj] = 'x'
            elif ss_map[i][j] == 'C':
                for k in range(1, 4):
                    for d in range(4):
                        ni = i + (di[d]*k)
                        nj = j + (dj[d]*k)
                        if (0 <= ni < N) and (0 <= nj < N) and (ss_map[ni][nj] == 'H'):
                            ss_map[ni][nj] = 'x'
    # pprint(ss_map)
    # print()

    cnt = 0
    for i in range(M):
        for j in range(N):
            if ss_map[i][j] == 'H':
                cnt += 1
    print(f'#{tc} {cnt}')