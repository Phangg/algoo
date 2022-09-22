import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):           # arr 0행, 0열 누적 값 채워주기
        arr[0][i] += arr[0][i-1]
        arr[i][0] += arr[i-1][0]
    # print(arr)

    for i in range(1, N):           # (1,1) 에서, 이전 값 체크해서 쌓아가기
        for j in range(1, N):
            y = arr[i-1][j]         # 위쪽 값
            x = arr[i][j-1]         # 왼쪽 값
            if x > y:
                arr[i][j] += y
            else:
                arr[i][j] += x
    # print(arr)
    print(f'#{tc}', arr[N-1][N-1])