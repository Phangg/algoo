import sys
from pprint import pprint
sys.stdin = open('input.txt')

paper = [[0] * 1001 for _ in range(1001)]

# N : 색종이의 장수
N = int(sys.stdin.readline())
point = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(point)
n = 0
for x, y, p, q in point:
    n += 1
    for i in range(x, x+p):
        for j in range(y, y+q):
            paper[i][j] = n

# pprint(paper)

for n in range(1, N+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if paper[i][j] == n:
                cnt += 1
    print(cnt)
