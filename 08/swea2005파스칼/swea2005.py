import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')

    N = int(input())

    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j or j == 0:
                arr[i][j] = 1
            elif i >= 1:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    for A in arr:
        res =[]
        for a in A:
            if a != 0:
                res.append(a)
        print(*res)