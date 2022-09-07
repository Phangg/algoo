T = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for case in range(T):
    n = int(input())
    
    arr = [[0]*n for _ in range(n)]

    # 첫줄 바로 채워 넣음
    num = n+1
    arr[0] = list(range(1, n + 1))
    x, y = 0, n - 1

    d = 0
    move = n-1

    while move:
        for _ in range(2):
            for _ in range(move):
                x = x + dx[d]
                y = y + dy[d]
                arr[x][y] = num
                num+=1

            d = (d+1)%4
        move -= 1

    print(f'#{case+1}')
    for i in arr:
        print(*i)


