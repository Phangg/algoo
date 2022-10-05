import sys
sys.stdin = open('input.txt')

def f(n):
    res = []
    for i in range(1, 1 << n):
        tmp = []
        for j in range(0, n):
            if i & (1 << j):
                tmp.append(w_lst[j])
                if sum(tmp) > K:
                    continue
        if sum(tmp) == K:
            res.append(tmp)
    return res

N, K = map(int, sys.stdin.readline().split())
item_dict = dict()
w_lst = []
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    item_dict[w] = v
    w_lst.append(w)

ans_lst = f(N)
total = 0
for ans in ans_lst:
    for x in ans:
        total += item_dict.get(x)
print(total)