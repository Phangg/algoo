import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

n, m = N, M
# 최소 공약수
while m > 0:
    n, m = m, n % m
print(n)

# 최소 공배수
print(N * M // n)