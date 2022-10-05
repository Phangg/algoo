import sys
sys.stdin = open('input.txt')

def ncr(s):
    if len(ans) == M:
        print(*ans)
    else:
        for i in range(s, N):
            if n_lst[i] not in ans:
                ans.append(n_lst[i])
                ncr(i)
                ans.pop()

N, M = map(int, sys.stdin.readline().split())
n_lst = list(map(int, sys.stdin.readline().split()))
n_lst.sort()

ans = []
ncr(0)