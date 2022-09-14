import sys
import math
sys.stdin = open('input.txt')

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    c = math.ceil(len(lst)/2)
    left = lst[:c]
    right = lst[c:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)

def merge(left, right):
    global cnt
    i, j = 0, 0
    tmp = []
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            tmp.append(left[i])
            cnt += 1
            if cnt == K:
                print(tmp[-1])
            i += 1
        else:
            tmp.append(right[j])
            cnt += 1
            if cnt == K:
                print(tmp[-1])
            j += 1
    while i < len(left):
        tmp.append(left[i])
        cnt += 1
        if cnt == K:
            print(tmp[-1])
        i += 1
    while j < len(right):
        tmp.append(right[j])
        cnt += 1
        if cnt == K:
            print(tmp[-1])
        j += 1
    return tmp

A, K = map(int, sys.stdin.readline().split())
a_lst = list(map(int, sys.stdin.readline().split()))
# print(A, K)
# print(a_lst)
cnt = 0
res = merge_sort(a_lst)
# print(cnt)
if cnt < K:
    print(-1)