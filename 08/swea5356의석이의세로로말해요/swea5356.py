import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    a_lst = [[None] * 15 for _ in range(15)]
    lst = [list(input()) for _ in range(5)]

    for i in range(5):
        for j in range(len(lst[i])):
            a_lst[i][j] = lst[i][j]

    ans_lst = []
    for x in range(15):
        for y in range(15):
            ans_lst.append(a_lst[y][x])

    res = ''
    for c in ans_lst:
        if c != None:
            res += c
    print(f'#{tc} {res}')