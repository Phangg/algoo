import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(N+1)]
# print(arr)
# print(dp)

for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i-1][2]

print(min(dp[N][0], dp[N][1], dp[N][2]))