import sys
sys.stdin = open('input.txt')

def ncr(s):
    if len(ans) == M:
        print(*ans)
    else:
        for i in range(1, N+1):
            ans.append(i)
            ncr(i)
            ans.pop()


N, M = map(int, sys.stdin.readline().split())

ans = []
ncr(1)