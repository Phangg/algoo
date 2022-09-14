import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    # print(lst)

    q = deque(lst)
    # print(q)
    goal = M
    cnt = 0
    ans = []
    while q:
        mm = max(q)
        x = q.popleft()
        M -= 1
        if mm == x:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            q.append(x)
            if M < 0:
                M = len(q) - 1