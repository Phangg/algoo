import sys
sys.stdin = open('6485input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_num = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    c_lst = []
    for _ in range(P):
        c_lst.append(int(input()))
    res = [0] * 5001
    # print(bus_num)
    # print(c_lst)


    for num in bus_num:
        for i in range(num[0], num[1]+1):
            res[i-1] += 1
    # print(res)
    ans = []
    for c in c_lst:
        ans.append(res[c-1])
    print(f'#{tc}', *ans)