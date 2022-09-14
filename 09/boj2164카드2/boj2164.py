import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
q = deque(list(range(1, N+1)))
# print(q)
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(*q)