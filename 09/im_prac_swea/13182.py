import sys
sys.stdin = open('13182input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    if lst[0] < M:
        print(f'#{tc}', 'Impossible')
        continue
    else:
        pain = 0
        sell = 0
        nope = 0
        for n in lst:
            pain = (n//M)*K - sell
            if pain <= 0:
                nope = 1
                break
            sell += 1
        if nope:
            print(f'#{tc}', 'Impossible')
        else:
            print(f'#{tc}', 'Possible')