import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [[0] * N for _ in range(N)]

    x, y = 0, 0
    lst[x][y] = 1
    n = 2
    while n < (N * N) + 1:
        while y + 1 < N and lst[x][y+1] == 0:
            y += 1
            lst[x][y] = n
            n += 1
        while x + 1 < N and lst[x+1][y] == 0:
            x += 1
            lst[x][y] = n
            n += 1
        while y > 0 and lst[x][y-1] == 0:
            y -= 1
            lst[x][y] = n
            n += 1
        while x > 0 and lst[x-1][y] == 0:
            x -= 1
            lst[x][y] = n
            n += 1

    print(f'#{tc}')
    for row in lst:
        print(*row)