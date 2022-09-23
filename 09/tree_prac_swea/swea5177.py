import sys
sys.stdin = open('5177input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    for i in range(2, N+1):
        c = i
        p = (i//2)
        while p and lst[p] > lst[c]:
            lst[p], lst[c] = lst[c], lst[p]
            c = p
            p = (c//2)
    # print(lst)
    ans = 0
    while N >= 1:
        ans += (lst[N//2])
        N //= 2
    print(f'#{tc} {ans}')


# def make_tree(n, c):
#     tree[c] = n
#     p = c//2
#     while tree[p] > n:
#         tree[c], tree[p] = tree[p], tree[c]
#         c = p
#         p = c//2
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     # print(lst)
#     tree = [0] * (N+1)
#
#     idx = 1
#     for num in lst:
#         make_tree(num, idx)
#         idx += 1
#     # print(tree)
#     # print(tree[N])
#
#     ans = 0
#     while N >= 1:
#         x = tree[N//2]
#         ans += x
#         N //= 2
#     print(f'#{tc} {ans}')