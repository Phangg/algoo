import sys
sys.stdin = open('15200input.txt')

def max_check(x, y):
    max_s = 0
    for i in range(0, len(y)-len(x)+1):
        s = 0
        for j in range(len(x)):
            s += (x[j] * y[i+j])
        if max_s < s:
            max_s = s
    return max_s

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 0
    if N >= M:
        ans = max_check(B, A)
    elif N < M:
        ans = max_check(A, B)
    print(f'#{tc} {ans}')