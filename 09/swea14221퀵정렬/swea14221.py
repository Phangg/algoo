import sys
sys.stdin = open('input.txt')


def q_s(lst, l, r):
    if l < r:
        piv = p(lst, l, r)
        q_s(lst, l, piv-1)
        q_s(lst, piv+1, r)
    # return lst

def p(lst, l, r):
    piv = lst[r]
    i = l-1
    for j in range(l, r):
        if lst[j] <= piv:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[r], lst[i+1] = lst[i+1], lst[r]
    return i+1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    q_s(lst, 0, N-1)
    # print(lst)
    print(f'#{tc}', lst[N//2])