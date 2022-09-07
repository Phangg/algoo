import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # print(N, M)
    nums = list(map(int, input().split()))
    # print(nums)
    cq = deque()
    for n in nums:
        cq.append(n)
    # print(cq)

    cnt = 0
    while cnt < M:
        x = cq.popleft()
        cq.append(x)
        cnt += 1
    print(f'#{tc} {cq[0]}')