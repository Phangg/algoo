import sys
sys.stdin = open('input.txt')

def ans(X):                                 # 반복 -> 재귀 구성
    if X == 10:                             # 길이가 10일 경우 1가지 방법
        return 1
    elif X == 20:                           # 길이가 20일 경우 3가지 방법
        return 3
    else:
        return (2 * ans(X-20)) + ans(X-10)  # 반복

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}', ans(N))