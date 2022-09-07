import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

ans = 65
for x in range(N - 8 + 1):                                  # 8 * 8 체스판으로 잘라서 볼 것임
    for y in range(M - 8 + 1):
        cnt = 0                                             # b -> w  / w -> b 상황별 카운트
        r_cnt = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if i%2:
                    if j%2 and board[i][j] == 'W':
                        cnt += 1
                    elif j%2==0 and board[i][j] == 'B':
                        cnt += 1
                else:
                    if j%2 and board[i][j] == 'B':
                        cnt += 1
                    elif j%2==0 and board[i][j] == 'W':
                        cnt += 1
                if i%2:
                    if j%2 and board[i][j] == 'B':
                        r_cnt += 1
                    elif j%2==0 and board[i][j] == 'W':
                        r_cnt += 1
                else:
                    if j%2 and board[i][j] == 'W':
                        r_cnt += 1
                    elif j%2==0 and board[i][j] == 'B':
                        r_cnt += 1
        ans = min(cnt, r_cnt, ans)
print(ans)
