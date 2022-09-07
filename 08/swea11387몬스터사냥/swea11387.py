import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    D, L, N = map(int, input().split())

    lst = []
    for n in range(N):
        lst.append(D * (1 + n * L / 100))

    S = 0
    for i in lst:
        S += i
    print(f'#{tc} {int(S)}')