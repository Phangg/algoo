import sys
sys.stdin = open('input.txt')

def knapsack(c, n):
    if c == 0 or n == 0:
        return 0
    if w_lst[n-1] > c:
        return knapsack(c, n-1)
    else:
        return max(v_lst[n-1] + knapsack(c - w_lst[n-1], n-1), knapsack(c, n-1))


N, K = map(int, sys.stdin.readline().split())
w_lst, v_lst = [], []
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    w_lst.append(w)
    v_lst.append(v)

print(knapsack(K, N))

