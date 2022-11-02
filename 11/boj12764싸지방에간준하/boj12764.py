import sys
import heapq
from collections import defaultdict
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
com_use_lst = []
for _ in range(n):
    p, q = map(int, sys.stdin.readline().split())
    heapq.heappush(com_use_lst, (p, q))
# print(com_use_lst)

com_dict = defaultdict(tuple)
max_t = 0
min_t = 0
for i in range(n):
    tmp_t = heapq.heappop(com_use_lst)
    if max_t < tmp_t[1]:
        max_t = tmp_t[1]
    if min_t > tmp_t[0]:
        min_t = tmp_t[0]
    if
    com_dict[i+1] =
print(com_dict)