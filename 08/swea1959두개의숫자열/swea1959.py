import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N <= M:
        max_ans = 0
        for i in range(M-N+1):
            sub_ans = 0
            for j in range(N):
                sub_ans += A[j] * B[i+j]
            if max_ans < sub_ans:
                max_ans = sub_ans

    if M < N:
        max_ans = 0
        for i in range(N-M+1):
            sub_ans = 0
            for j in range(M):
                sub_ans += A[i+j] * B[j]
            if max_ans < sub_ans:
                max_ans = sub_ans

    print(f'#{tc} {max_ans}')