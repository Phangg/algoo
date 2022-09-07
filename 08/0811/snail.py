t = int(input()) 

for case in range(t):

    n = int(input()) 
    lst = [[0] * n for _ in range(n)] 
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 0, -1
    d = 0

    num = 0
    while num < n**2:

        nx = x + dx[d]
        ny = y + dy[d]
        if 0<= nx < n and 0<= ny < n and lst[nx][ny] == 0:
            x = nx
            y = ny
            num += 1
            lst[x][y] = num
        else:
            d = (d+1)%4

    for line in lst:
        print(*line)
