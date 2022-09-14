import sys
sys.stdin = open('input.txt')

def facto(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

# 이항 계수 => n C k => n! / (n-k)! * k!

N, K = map(int, sys.stdin.readline().split())

res = facto(N) // (facto(K) * facto(N-K))
print(res)