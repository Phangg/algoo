import sys
sys.stdin = open('input.txt')

def p(i, k, r):
    if i == r:
        print(*ans)
    else:
        for j in range(k):
            if not used[j]:
                used[j] = 1
                ans[i] = n_lst[j]
                p(i+1, k, r)
                used[j] = 0

N, M = map(int, sys.stdin.readline().split())
n_lst = list(map(int, sys.stdin.readline().split()))
n_lst.sort()

ans = [0] * M
used = [0] * N
p(0, N, M)