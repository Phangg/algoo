import sys
sys.stdin = open('input.txt')

def super_sum(_arr):        # 2차원 배열 합 구해주는 함수
    s = 0
    for x in _arr:
        s += sum(x)
    return s

def check(lst, n):
    global w_cnt, b_cnt
    if n == 2:
        lst_s = super_sum(lst)      # lst_s : n 이 2일때, 2차원 배열의 합
        if lst_s == 0:
            w_cnt += 1              # 다 0 이면 w + 1
        elif lst_s == 1:
            w_cnt += 3              # 1 이면 b + 1 / w + 3
            b_cnt += 1
        elif lst_s == 2:
            w_cnt += 2              # 2 이면 b + 2 / w + 2
            b_cnt += 2
        elif lst_s == 3:
            w_cnt += 1              # 3 이면 b + 3 / w + 1
            b_cnt += 3
        else:
            b_cnt += 1              # 다 4 면 b + 1
    else:
        nn = n//2
        arr1 = list(map(lambda x: x[:nn], lst[:nn]))        # nn 행 까지 슬라이싱해서 -> nn 열 까지 슬라이싱 맵핑
        arr2 = list(map(lambda x: x[nn:], lst[:nn]))
        arr3 = list(map(lambda x: x[:nn], lst[nn:]))
        arr4 = list(map(lambda x: x[nn:], lst[nn:]))
        for x in [arr1, arr2, arr3, arr4]:
            tmp_s = super_sum(x)                            # tmp_s : 분할 된 2차원 배열의 합
            if tmp_s == 0:
                w_cnt += 1
            elif tmp_s == nn**2:
                b_cnt += 1
            else:                                           # b나 w가 아니면, 재귀
                check(x, nn)


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

w_cnt, b_cnt = 0, 0
arr_s = super_sum(arr)                          # arr_s : 초기 2차원 배열 합
if arr_s == 0:
    w_cnt += 1                                  # 초기 상태 확인 위해서, 초기 2차원 배열 합 체크
elif arr_s == N**2:
    b_cnt += 1
else:
    check(arr, N)

print(w_cnt)
print(b_cnt)
