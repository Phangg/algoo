import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = []
    for i in range(N-1):
        for j in range(i+1, N):
            ans.append(lst[i] * lst[j])
    # print(ans)

    res = []
    for num in ans:
        if num//10:
            n_lst = [int(a) for a in str(num)]
            # print(n_lst)
            for k in range(len(n_lst)-1, 0, -1):
                if n_lst[k] < n_lst[k-1]:
                    break
            else:
                xx = ''
                for x in n_lst:
                    xx += str(x)
                res.append(int(xx))
    # print(res)
    if res:
        print(f'#{tc} {max(res)}')
    else:
        print(f'#{tc}', -1)


# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     res = -1
#     for i in range(N-1):
#         for j in range(i+1, N):
#             s = lst[i]*lst[j]
#             print(s)
#             s_ori = lst[i]*lst[j]
#             if s < 10:
#                 continue
#             while s >= 1:
#                 na = s % 10
#                 s = s//10
#                 if na < s % 10:
#                     break
#             else:
#                 if res < s_ori:
#                     res = s_ori
#     print(f'#{t} {res}')