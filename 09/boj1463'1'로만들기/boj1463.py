import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

dp = [0] * (N+1)

for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1                 # 아무것도 아닐때 -1 할거라서
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)  # 만약 나눠질때, 그 전으로 돌아갔을때랑 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[N])