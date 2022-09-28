import sys
sys.stdin = open('13672input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    i, j = 0, -1
    for num in range(1, (N*N)+1):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if (0 <= ni < N) and (0 <= nj < N) and not arr[ni][nj]:
                arr[ni][nj] = num
                i, j = ni, nj
                break
    print(f'#{tc}')
    for a in arr:
        print(*a)