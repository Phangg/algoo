import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    arr_h = list(map(list, zip(*arr)))  # 세로로 돌린 2차원 리스트

    ans = ''
    for i in range(n):
        for j in range(0, n-m+1):

            if arr[i][j:m+j] == arr[i][j:m+j][::-1]:
                ans = arr[i][j:m + j]
                print(f'#{tc}', ''.join(ans))

            if arr_h[i][j:m+j] == arr_h[i][j:m+j][::-1]:
                ans = arr_h[i][j:m + j]
                print(f'#{tc}', ''.join(ans))

