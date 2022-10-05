import sys
sys.stdin = open('input.txt')

def f(s):
    if len(ans) == M:
        print(*ans)
    else:
        for i in range(s, N+1):
            ans.append(i)
            f(i)
            ans.pop()


N, M = map(int, sys.stdin.readline().split())

ans = []
f(1)
