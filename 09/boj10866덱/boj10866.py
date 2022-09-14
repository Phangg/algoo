import sys
from collections import deque
sys.stdin = open('input.txt')

q = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    order = sys.stdin.readline().rstrip()

    if ' ' in order:
        o, num = order.split()
        if o == 'push_back':
            q.append(num)
        else:
            q.appendleft(num)
    elif order == 'pop_front':
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)
    elif order == 'pop_back':
        if q:
            x = q.pop()
            print(x)
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)