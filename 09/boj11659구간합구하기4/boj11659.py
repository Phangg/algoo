import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
hap = [0] * N
plus = 0
for idx, num in enumerate(nums):
    plus += num
    hap[idx] = plus
# print(hap)
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    if s-1:
        print(hap[e-1] - hap[s-1-1])
    else:
        print(hap[e-1])