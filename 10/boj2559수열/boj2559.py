import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

tmp = sum(lst[:K])
max_v = tmp
for i in range(1, N-K+1):
    tmp = tmp - lst[i-1] + lst[i+K-1]
    if max_v < tmp:
        max_v = tmp
print(max_v)