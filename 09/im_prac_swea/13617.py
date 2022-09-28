import sys
sys.stdin = open('13617input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * (N+1)
    for i in range(Q):
        L, R = map(int, input().split())
        box[L:R+1] = [i+1] * (R-L+1)
    print(f'#{tc}', *box[1:])