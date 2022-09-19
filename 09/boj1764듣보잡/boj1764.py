import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
no_h = set(sys.stdin.readline().rstrip() for _ in range(N))
no_s = set(sys.stdin.readline().rstrip() for _ in range(M))

x = no_h - no_s

ans = no_h - x
ans = sorted(ans)
print(len(ans))
for a in ans:
    print(a)