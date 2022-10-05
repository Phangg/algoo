import sys
sys.stdin = open('15701input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    tmp_arr = [list(map(int, input().split())) for _ in range(N)]
    arr = list(map(list, zip(*tmp_arr)))

    # 1 : 빨강 / N -> S , 2: 파랑 / S -> N

    ans = 0
    for line in arr:
        tmp = 0
        for x in line:
            if x == 1:
                tmp = 1
            elif x == 2 and tmp == 1:
                ans += 1
                tmp = 2
    print(f'#{tc} {ans}')