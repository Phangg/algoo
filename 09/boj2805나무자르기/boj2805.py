import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
tree_h = list(map(int, sys.stdin.readline().split()))
# print(tree_h)

s = 1
e = 2000000000
while s <= e:
    ttt = 0
    mid = (s + e)//2
    for tr in tree_h:
        if tr > mid:
            ttt += (tr - mid)
    if ttt >= M:
        s = mid + 1
    else:
        e = mid - 1
print(e)