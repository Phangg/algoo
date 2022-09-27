import sys
sys.stdin = open('input.txt')

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(l, r):
    global cnt
    res = []

    if l[-1] > r[-1]:
        cnt += 1

    l = l[::-1]
    r = r[::-1]
    while l or r:
        if l and r:
            if l[-1] >= r[-1]:
                res.append(r.pop())
            else:
                res.append(l.pop())
        elif l:
            res.extend(l[::-1])
            break
        elif r:
            res.extend(r[::-1])
            break
    return res


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    sort_list = merge_sort(lst)
    # print(sort_list)
    print(f'#{tc} {sort_list[N//2]} {cnt}')