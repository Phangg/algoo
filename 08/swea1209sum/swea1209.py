import sys
sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]


    max_sum = 0  # 제일 큰 합
    for i in range(100):
        sum_x = sum_y = 0  # 행의 합 / 열의 합
        for j in range(100):
            sum_x += lst[i][j]
            sum_y += lst[j][i]
        if sum_x > max_sum:
            max_sum = sum_x
        if sum_y > max_sum:
            max_sum = sum_y

    sum_v = 0  # 좌상우하 대각선
    sum_w = 0  # 우상좌하 대각선
    for i in range(100):
        sum_v += lst[i][i]
        sum_w += lst[i][100-i-1]
    if sum_v > max_sum:
        max_sum = sum_v
    if sum_w > max_sum:
        max_sum = sum_w

    print(f'#{t} {max_sum}')

    '''
    sum_lst = max(list(map(sum, lst)))  # 가로 행의 합 중에 최대 값
    lst_trans = zip(*lst)  # 세로를 만들기 위해 옆으로 돌리기
    sum_lst_trans = max(list(map(sum, lst_trans)))  # 세로 행 중에 최대 값
    sum_dia = sum([lst[i][i] for i in range(n)])  # 좌상우하 대각선 합
    sum_dia_reverse = sum([lst[-i][-i-1] for i in range(n)])  # 우상좌하 대각선 합 
    '''