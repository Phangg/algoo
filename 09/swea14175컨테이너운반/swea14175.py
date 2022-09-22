import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w_lst = sorted(list(map(int, input().split())), reverse=True)
    t_lst = sorted(list(map(int, input().split())))
    # print(w_lst)
    # print(t_lst)

    ans = 0
    for t in t_lst:
        for idx, w in enumerate(w_lst):
            if t >= w:
                ans += w
                w_lst[idx] = 51             # 문제에서 주는 범위 밖의 최소 값
                break
    print(f'#{tc} {ans}')