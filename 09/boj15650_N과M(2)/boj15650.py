import sys
sys.stdin = open('input.txt')

def nCr(s):
    if len(ans) == M:
        print(*ans)
    else:
        for i in range(s, N+1):
            if i not in ans:
                ans.append(i)
                nCr(i+1)
                ans.pop()

N, M = map(int, sys.stdin.readline().split())

ans = []
nCr(1)