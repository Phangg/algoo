import sys
sys.stdin = open('input.txt')

# 피보나치 수열
# 재귀보다 DP가 더 빠르다!

def fib1(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    f = [0]*(n+1)
    f[1] = f[2] = 1
    cnt = 0
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        cnt += 1
    return cnt

N = int(sys.stdin.readline())

print(fib1(N), fib2(N))