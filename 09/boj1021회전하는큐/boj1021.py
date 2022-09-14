import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
num_id = list(map(int, sys.stdin.readline().split()))

cq = deque(list(range(1, N + 1)))
# print(cq)

cnt = 0
for i in range(M):
    if cq[0] != num_id[i]:
        if cq.index(num_id[i]) > cq.index(cq[(len(cq)-1)//2]):
            while cq[0] != num_id[i]:
                cq.appendleft(cq.pop())
                cnt += 1
        elif cq.index(num_id[i]) <= cq.index(cq[(len(cq)-1)//2]):
            while cq[0] != num_id[i]:
                cq.append(cq.popleft())
                cnt += 1
    cq.popleft()
# print(cq)
print(cnt)