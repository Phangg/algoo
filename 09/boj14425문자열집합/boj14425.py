import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
s = set(sys.stdin.readline().rstrip() for _ in range(N))
cnt = 0
for _ in range(M):
    if sys.stdin.readline().rstrip() in s:
        cnt += 1
print(cnt)