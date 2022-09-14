import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
q = deque(list(range(1, N+1)))
# print(q)
print('<', end='')
while len(q) > 1:
    for i in range(K-1):
        x = q.popleft()
        q.append(x)
    x = q.popleft()
    print(x, end=', ')
print(*q, end='')
print('>')