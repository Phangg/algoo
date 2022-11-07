import sys
sys.stdin = open('input.txt')

# 직접 적어보면 case1 + case2 = case3
# 1
# 12 / 21
# 123 / 132 / 213
# 1234 / 1243 / 2134 / 2143 / 1324

def check(n):
    if dp[n] > 0:
        return dp[n]
    elif n == 1:
        return 1
    else:
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
m = int(sys.stdin.readline())
vip = list(int(sys.stdin.readline()) for _ in range(m))
vip.append(n+1)
# print(vip)

if not m:
    print(check(n))
else:
    ans = 1
    tmp_v = 0
    for v in vip:
        ans *= check(v - 1 - tmp_v)
        tmp_v = v
    print(ans)