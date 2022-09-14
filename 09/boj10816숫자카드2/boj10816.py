import sys
from collections import Counter
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
N_lst = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_lst = list(map(int, sys.stdin.readline().split()))

cnt = Counter(N_lst)
for m in M_lst:
    print(cnt[m], end=' ')