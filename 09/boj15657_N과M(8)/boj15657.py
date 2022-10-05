import sys
sys.stdin = open('input.txt')

def f(s):
    if len(ans) == M:
        print(*ans)
    else:
        for i in range(s, N):
            ans.append(n_lst[i])
            f(i)
            ans.pop()


N, M = map(int, sys.stdin.readline().split())
n_lst = list(map(int, sys.stdin.readline().split()))
n_lst.sort()

ans = []
f(0)