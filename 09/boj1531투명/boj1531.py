import sys
sys.stdin = open('input.txt')

paint = [[0] * 101 for _ in range(101)]
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            paint[i][j] += 1

ans = 0
for i in range(1, 101):
    for j in range(1, 101):
        if paint[i][j] > M:
            ans += 1
print(ans)