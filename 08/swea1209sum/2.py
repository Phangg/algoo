import sys
sys.stdin = open('input.txt')

T = 10
N = 100

for _ in range(T):
    tc = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    re_lst = list(map(list, zip(*lst)))

    max_row = 0
    for row in lst:
        if max_row < sum(row):
            max_row = sum(row)

    max_col = 0
    for col in re_lst:
        if max_col < sum(col):
            max_col = sum(col)

    cr = 0
    rc = 0
    for i in range(N):
        cr += lst[i][i]
        rc += lst[i][-1-i]

    print(f'#{tc}', max(max_row, max_col, cr, rc))