import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0] * N

# 주어지는 포도잔의 수 (N)이 3보다 큰 경우
# 0, 1, 2 번 인덱스 값에 올 수 있는 최대 값 넣어주기
if N >= 4:
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(dp[1], lst[0]+lst[2], lst[1]+lst[2])            # 꼭 2번 인덱스가 아니어도 최대값이 될 수 있음..ㅠ
    for i in range(3, N):
        dp[i] = max(dp[i-2]+lst[i], dp[i-3]+lst[i-1]+lst[i])    # for 문을 돌면서 이후에 자리할 수 있는 최대값 넣어주기
        if dp[i] < dp[i-1]:
            dp[i] = dp[i-1]                                     # 0이 연속되면 누적 값이 낮아지는 경우가 생김 -> 이를 막아주기
    print(max(dp[N-4:N]))                                       # 최대값 출력

# 주어지는 포도잔의 수 (N)이 3보다 작을 경우마다 나누어서 출력
elif N == 3:
    print(max(lst[0] + lst[1], lst[0]+lst[2], lst[1]+lst[2]))   # 꼭 2번 인덱스가 아니어도 최대값이 될 수 있음..ㅠ
elif N == 2:
    print(lst[0]+lst[1])
else:
    print(lst[0])