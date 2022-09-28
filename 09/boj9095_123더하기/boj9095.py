import sys
sys.stdin = open('input.txt')

def dp(n):
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    return d[n]

T = int(sys.stdin.readline())
d = [0 for _ in range(11)]
d[1] = 1
d[2] = 2
d[3] = 4
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp(n))