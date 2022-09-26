import sys
sys.stdin = open('1954input.txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    d = 0
    x, y = 0, 0
    for i in range(1, N*N+1):
        arr[x][y] = i
        nx, ny = x+dx[d], y+dy[d]
        if (0 <= nx < N) and (0 <= ny < N) and (arr[nx][ny] == 0):
            x, y = nx, ny
        else:
            d = (d+1) % 4
            nx, ny = x + dx[d], y + dy[d]
            x, y = nx, ny
    # print(arr)

    print(f'#{tc}')
    for ans in arr:
        print(*ans)