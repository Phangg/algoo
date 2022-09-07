import sys
sys.stdin = open('input.txt')

def end_point(ladder, N):
    for n in range(N):
        if ladder[-1][n] == 2:
            return n
    return

#    우  상  좌
di = [0, -1, 0]
dj = [1, 0, -1]

T = 10
N = 100
for _ in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]

    x, y = N-1, end_point(ladder, N)

    while x > 0:
        for d in range(3):
            nx = x + di[d]
            ny = y + dj[d]
            if (0 <= nx < N) and (0 <= ny < N) and (ladder[nx][ny] == 1):
                ladder[nx][ny] = 0
                x = nx
                y = ny

    print(f'#{tc} {y}')