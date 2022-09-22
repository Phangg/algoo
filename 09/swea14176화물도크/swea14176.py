import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        lst.append([s, e])
    lst = sorted(lst, key=lambda x: (x[1], x[0]))
    # print(lst)

    ans = 1
    end = lst[0][1]
    for i in range(1, N):
        if end <= lst[i][0]:
            end = lst[i][1]
            ans += 1
    print(f'#{tc} {ans}')