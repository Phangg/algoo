import sys
sys.stdin = open('12712input.txt')

def check_1(x, y):
    res = arr[x][y]
    k = 1
    while k < M:
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x+(dx*k), y+(dy*k)
            if (0 <= nx < N) and (0 <= ny < N):
                res += arr[nx][ny]
        k += 1
    return res

def check_2(x, y):
    res = arr[x][y]
    k = 1
    while k < M:
        for dx, dy in [[-1, 1], [1, 1], [1, -1], [-1, -1]]:
            nx, ny = x+(dx*k), y+(dy*k)
            if (0 <= nx < N) and (0 <= ny < N):
                res += arr[nx][ny]
        k += 1
    return res

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    max_death = 0
    for i in range(N):
        for j in range(N):
            a = check_1(i, j)
            b = check_2(i, j)
            max_death = max(a, b, max_death)
    print(f'#{tc} {max_death}')
