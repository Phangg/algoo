import sys
sys.stdin = open('input.txt')

T = 10
N = 8
for tc in range(1, T+1):
    X = int(input())
    lst = [list(input()) for _ in range(N)]
    re_lst = list(map(list, zip(*lst)))

    cnt = 0
    for row in lst:
        for j in range(N-X+1):
            if row[j:j+X] == row[j:j+X][::-1]:
                cnt += 1

    for col in re_lst:
        for j in range(N-X+1):
            if col[j:j+X] == col[j:j+X][::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')