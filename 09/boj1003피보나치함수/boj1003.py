import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
N_lst = [int(sys.stdin.readline().rstrip()) for _ in range(T)]
# print(N_lst)

dp = [[0, 0] for _ in range(41)]            # 0 <= N <= 40
dp[0] = [1, 0]                              # 0은 0을 출력 dp[0][0] -> 0
dp[1] = [0, 1]                              # 1은 1을 출력 dp[1][1] -> 1

if max(N_lst) > 1:                          # 최대 값이 1보다 클때 탐색하기
    for i in range(2, max(N_lst)+1):        # 2 ~ 최대값까지
        dp[i][0] = dp[i-1][0] + dp[i-2][0]  # 0이 나온 횟수
        dp[i][1] = dp[i-1][1] + dp[i-2][1]  # 1이 나온 횟수
# print(dp)
for num in N_lst:
    print(*dp[num])




# def fibo(n):
#     global a, b
#     if n == 0:
#         a += 1
#         return 0
#     elif n == 1:
#         b += 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# T = int(sys.stdin.readline())
# for _ in range(T):
#     a = b = 0
#     N = int(sys.stdin.readline())
#     fibo(N)
#     print(a, b)