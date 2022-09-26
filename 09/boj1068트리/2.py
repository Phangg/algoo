from collections import defaultdict
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def pre_order(root):
    global cnt
    if len(ch_dict[root]) == 0:
        cnt += 1
    else:
        while ch_dict[root]:
            pre_order(ch_dict[root][-1])
            ch_dict[root].pop()


ch_dict = defaultdict(list)
p_dict = defaultdict(list)
cnt = 0

n = int(input())
tree = map(int, input().split())
rmv = int(input())

for i in range(n):
    ch_dict[i] = []

for j, e in enumerate(tree):
    if e == -1:
        root = j
    else:
        ch_dict[e] += [j]
        p_dict[j] += [e]

if p_dict[rmv]:
    live_node = p_dict[rmv][0]
    idx = ch_dict[live_node].index(rmv)
    if ch_dict[rmv]:
        del(ch_dict[rmv])
        ch_dict[live_node].pop(idx)
    else:
        ch_dict[live_node].pop(idx)
    pre_order(root)
else:
    cnt = 0
print(cnt)