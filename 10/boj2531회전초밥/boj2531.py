import sys
from collections import defaultdict
sys.stdin = open('input.txt')

n, d, k, c = map(int, sys.stdin.readline().split())
lst = list(int(sys.stdin.readline().rstrip()) for _ in range(n))

eat = defaultdict(int)
cnt = 1
eat[c] = 1
for i in range(k):
    if eat[lst[i]] == 0:
        cnt += 1
    eat[lst[i]] += 1

answer = cnt
for left in range(n):
    right = (left+k) % n
    eat[lst[left]] -= 1
    if eat[lst[left]] == 0:
        cnt -= 1
    if eat[lst[right]] == 0:
        cnt += 1
    eat[lst[right]] += 1
    answer = max(answer, cnt)
print(answer)

# ---------------------------------------------------------------------------------------------------------------

# pypy 만 통과

# max_len = 0
# for i in range(n):
#     tmp = set()
#     flag = 0
#     for j in range(k):
#         x = i + j
#         if x >= n:
#             x -= n
#         tmp.add(lst[x])
#         if lst[x] == c:
#             flag = 1
#
#     if max_len <= len(tmp):
#         if flag:
#             max_len = len(tmp)
#         else:
#             max_len = len(tmp)+1
# print(max_len)