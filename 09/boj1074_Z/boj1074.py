import sys
sys.stdin = open('input.txt')

def divide(n, r, c):
    global cnt
    if n == 2:
        if r == 0 and c == 0:
            cnt += 0
        elif r == 0 and c:
            cnt += 1
        elif r and c == 0:
            cnt += 2
        else:
            cnt += 3
    else:
        if r < n//2 and c < n//2:                           # 좌 상
            divide(n//2, r, c)
        elif r < n//2 and c >= n//2:                        # 우 상
            cnt += (n*n)//4
            divide(n//2, r, c-(n//2))
        elif r >= n//2 and c < n//2:                        # 좌 하
            cnt += (n*n)//4 * 2
            divide(n//2, r-(n//2), c)
        elif r >= n//2 and c >= n//2:                       # 우 하
            cnt += (n*n)//4 * 3                             # ex) n=8, 각 사각형의 첫값 시작 = 16*i
            divide(n//2, r-(n//2), c-(n//2))


N, r, c = map(int, sys.stdin.readline().split())

cnt = 0
divide(2**N, r, c)
print(cnt)