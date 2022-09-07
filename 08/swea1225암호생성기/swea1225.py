import sys
from collections import deque
sys.stdin = open('input.txt')


T = 10
for _ in range(T):
    tc = int(input())
    D = list(map(int, input().split()))

    cq = deque()
    for d in D:
        cq.append(d)

    x = cq[0]
    i = 1
    while 1:
        x = cq.popleft()
        if x-i <= 0:
            cq.append(0)
            break
        cq.append(x-i)
        i = (i % 5) + 1

    print(f'#{tc}', *cq)

