# 모든 리스트 idx 0,1 / -1,-2 는 0이 들어있음
# 왼쪽, 오른쪽 각각 2개 idx 의 value 는 나보다 작아야 함

import sys
sys.stdin = open('input.txt')

def my_min(a, b, c, d):
    result = a
    if a > b:
        result = b
    if result > c:
        result = c
    if result > d:
        result = d
    return result

T = 10
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2):
        left_1 = lst[i] - lst[i-1]
        left_2 = lst[i] - lst[i-2]
        right_1 = lst[i] - lst[i+1]
        right_2 = lst[i] - lst[i+2]

        if left_1 > 0 and left_2 > 0 and right_2 > 0 and right_1 > 0:
            cnt += my_min(left_1, left_2, right_1, right_2)
    print(f'#{tc} {cnt}')
