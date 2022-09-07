import sys
sys.stdin = open('input.txt')

T = int(input())
N = 9
for tc in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(N)]
    re_lst = list(map(list, zip(*lst)))

    ans = 1

    for row in lst:
        x = set(row)
        if len(x) != N:
            ans = 0

    for col in re_lst:
        y = set(col)
        if len(y) != N:
            ans = 0

    tmp = []
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            for p in range(3):
                for q in range(3):
                    tmp.append(lst[i+p][j+q])
            z = set(tmp)
            if len(z) != N:
                ans = 0
            tmp = []

    print(f'#{tc} {ans}')