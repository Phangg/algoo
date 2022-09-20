import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    # print(N)
    ans = ''
    i = -1
    while N != 0:
        x, N = divmod(N, 2**i)
        ans += str(int(x))
        i -= 1

    if len(ans) > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {ans}')