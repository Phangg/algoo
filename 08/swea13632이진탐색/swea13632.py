import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    P, pa, pb = map(int, input().split())

    A_cnt = 0
    a_start = 1
    a_end = P
    while a_start <= a_end:
        a_mid = (a_start + a_end) // 2
        if pa == a_mid:
            A_cnt += 1
            break
        elif pa > a_mid:
            a_start = a_mid
            A_cnt += 1
        else:
            a_end = a_mid
            A_cnt += 1

    B_cnt = 0
    b_start = 1
    b_end = P
    while b_start <= b_end:
        b_mid = (b_start + b_end) // 2
        if pb == b_mid:
            B_cnt += 1
            break
        elif pb > b_mid:
            b_start = b_mid
            B_cnt += 1
        else:
            b_end = b_mid
            B_cnt += 1

    if A_cnt < B_cnt:
        print(f'#{tc}', 'A')
    elif A_cnt > B_cnt:
        print(f'#{tc}', 'B')
    else:
        print(f'#{tc}', 0)