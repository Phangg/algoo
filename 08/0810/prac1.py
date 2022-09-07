# 연습 문제 1
import sys
sys.stdin = open('prac1_input.txt')

# 우 하 좌 상 순서
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    sum_all = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    num = lst[i][j] - lst[ni][nj]
                    abs_n = abs(num)
                    sum_all += abs_n

    print(f'#{tc} {sum_all}')
