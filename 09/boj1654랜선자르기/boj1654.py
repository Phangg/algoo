import sys
import math
sys.stdin = open('input.txt')

K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
lan.sort()
s = 1
e = lan[-1]

ans = 0
while s <= e:
    cnt = 0
    mid = math.ceil((s + e)/2)
    for ll in lan:
        cnt += (ll // mid)
    if cnt >= N:                    # 최대 값을 찾기 위함으로 cnt == N 이더라도, 계속 탐색
        s = mid + 1                 # e를 s가 넘어서려고 하면 중단 / 그 때 가지고 있던 e 값이 최대
    elif cnt < N:
        e = mid - 1
print(e)
