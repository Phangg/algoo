import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        sub_cnt = 0
        for j in range(M):
            if lst[i][j] == 1:
                sub_cnt += 1
                if cnt < sub_cnt:
                    cnt = sub_cnt
            else:
                sub_cnt = 0

    for i in range(M):
        sub_cnt = 0
        for j in range(N):
            if lst[j][i] == 1:
                sub_cnt += 1
                if cnt < sub_cnt:
                    cnt = sub_cnt
            else:
                sub_cnt = 0

    print(f'#{tc} {cnt}')