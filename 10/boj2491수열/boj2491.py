import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
max_v = 1

num = lst[0]
cnt = 1
for i in range(1, N):
    if lst[i] >= num:
        num = lst[i]
        cnt += 1
        if max_v < cnt:
            max_v = cnt
    else:
        num = lst[i]
        cnt = 1
        if max_v < cnt:
            max_v = cnt

num = lst[0]
cnt = 1
for i in range(1, N):
    if lst[i] <= num:
        num = lst[i]
        cnt += 1
        if max_v < cnt:
            max_v = cnt
    else:
        num = lst[i]
        cnt = 1
        if max_v < cnt:
            max_v = cnt
print(max_v)
