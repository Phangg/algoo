import sys
sys.stdin = open('input.txt')

def f(i, r):
    if i == r:
        print(*ans)
    else:
        for j in range(N):
            if not used[j]:
                used[j] = 1
                ans[i] = n_lst[j]
                f(i+1, r)
                used[j] = 0



N, M = map(int, sys.stdin.readline().split())
n_lst = [x for x in range(1, N+1)]

used = [0] * N
ans = [0] * M
f(0, M)
