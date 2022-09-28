import sys
sys.stdin = open('13999input.txt')

def dia():
    max_dia = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for x in range(1, M):
                for di, dj in [[-x, x], [x, x], [x, -x], [-x, -x]]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < N) and (0 <= nj < N):
                        s += arr[ni][nj]
            if max_dia < s:
                max_dia = s
    return max_dia


def cross():
    max_cross = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for x in range(1, M):
                for di, dj in [[0, x], [x, 0], [0, -x], [-x, 0]]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < N) and (0 <= nj < N):
                        s += arr[ni][nj]
            if max_cross < s:
                max_cross = s
    return max_cross


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    a = dia()
    b = cross()

    if a > b:
        print(f'#{tc} {a}')
    else:
        print(f'#{tc} {b}')