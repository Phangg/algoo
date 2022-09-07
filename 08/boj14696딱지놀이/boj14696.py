# 만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
# 별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.

import sys
sys.stdin = open('input.txt')

# 딱지 리스트에서 각 모양의 개수를 세어주는 함수
def check_figure(lst, a, b, c, d):
    star = lst.count(a)
    cir = lst.count(b)
    squ = lst.count(c)
    tri = lst.count(d)
    return [star, cir, squ, tri]


# N : 총 라운드 수
N = int(sys.stdin.readline())
# x_lst[0] 은 x가 내는 딱지 개수 / x_lst[1:] 가 x가 내는 딱지들
for _ in range(N):
    a_lst = list(map(int, sys.stdin.readline().split()))
    b_lst = list(map(int, sys.stdin.readline().split()))
    A_figure = a_lst[1:]
    B_figure = b_lst[1:]
    # print('a', a_lst[0], A_figure)
    # print('b', b_lst[0], B_figure)

    ans = None                                      # ans -> 결과 값 / D: 무 , A: a 승 , B: b 승

    A_cnt = check_figure(A_figure, 4, 3, 2, 1)      # 인덱스 0:별 , 1:동그 , 2:네모 , 3:세모
    B_cnt = check_figure(B_figure, 4, 3, 2, 1)
    # print(A_cnt)
    # print(B_cnt)

    if A_cnt[0] > B_cnt[0]:
        ans = 'A'
    elif A_cnt[0] < B_cnt[0]:
        ans = 'B'
    else:
        if A_cnt[1] > B_cnt[1]:
            ans = 'A'
        elif A_cnt[1] < B_cnt[1]:
            ans = 'B'
        else:
            if A_cnt[2] > B_cnt[2]:
                ans = 'A'
            elif A_cnt[2] < B_cnt[2]:
                ans = 'B'
            else:
                if A_cnt[3] > B_cnt[3]:
                    ans = 'A'
                elif A_cnt[3] < B_cnt[3]:
                    ans = 'B'
                else:
                    ans = 'D'
    print(ans)