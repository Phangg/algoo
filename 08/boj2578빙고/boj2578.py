import sys
sys.stdin = open('input.txt')

def bingocheck(lst):                    # 빙고 몇개 있는지 체크 (3개면 return)
    ans = 0
    for row in lst:                     # 행 체크
        if sum(row) == 0:
            ans += 1
            if ans == 3:
                return ans

    c_lst = list(map(list, zip(*lst)))  # 리스트 돌려서 열 체크
    for col in c_lst:
        if sum(col) == 0:
            ans += 1
            if ans == 3:
                return ans

    cross_cnt = 0                       # 좌상우하 대각선
    for x in range(5):
        if lst[x][x] == 0:
            cross_cnt += 1
            if cross_cnt == 5:
                ans += 1
                if ans == 3:
                    return ans

    re_cross_cnt = 0                    # 우상좌하 대각선
    for x in range(5):
        if lst[x][-x-1] == 0:
            re_cross_cnt += 1
            if re_cross_cnt == 5:
                ans += 1
                if ans == 3:
                    return ans
    else:
        return ans

num_lst = []
bingo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
for _ in range(5):
    nums = list(map(int, sys.stdin.readline().split()))
    for n in nums:
        num_lst.append(n)
# print(num_lst)
# print(bingo)
empty_lst = [[1]*5 for _ in range(5)]           # 1로 채워진 리스트 (여기서 빙고 체크)

res = 0
for num in num_lst:                             # 불러주는 숫자
    res += 1                                    # 숫자 불러 줄 때 마다 + 1
    flag = 0                                    # ij 맞았을 때, break 나오기 위한 플래그
    for i in range(5):
        for j in range(5):
            if num == bingo[i][j]:              # 불러주는 숫자가 빙고판 숫자와 같을 때
                empty_lst[i][j] = 0             # 빙고판의 해당 위치 -> empty_lst 의 같은 위치에 체크
                flag = 1
                break
        if flag:
            break

    if res > 10:                                # 못해도 숫자 10개는 넘어야 빙고 3개 만드니까
        if bingocheck(empty_lst) == 3:          # num 마다 빙고체크 함수로 빙고 체크
            print(res)                          # 빙고 3개면 해당 인덱스 +1 (몇번째로 불러준 숫자?) 출력
            break

# def func(num):
#     for i in range(5):
#         for j in range(5):
#             if num == bingo[i][j]:
#                 empty_lst[i][j] = 0
#                 return
# for num in num_lst:
#     func(num)
