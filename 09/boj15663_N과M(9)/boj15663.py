import sys
sys.stdin = open('input.txt')

def f(s):
    if s == M:
        print(' '.join(map(str, ans)))
        return
    pre_v = 0
    for i in range(0, N):
        if not used_i[i] and pre_v != n_lst[i]:
            used_i[i] = 1
            ans.append(n_lst[i])
            pre_v = n_lst[i]
            f(s+1)
            ans.pop()
            used_i[i] = 0


N, M = map(int, sys.stdin.readline().split())
n_lst = list(map(int, sys.stdin.readline().split()))
n_lst.sort()

used_i = [0] * N
ans = []
f(0)
