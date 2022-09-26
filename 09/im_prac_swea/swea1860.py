import sys
sys.stdin = open('1860input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    person = list(map(int, input().split()))
    person.sort()
    ans = True
    sell = 0
    pain = 0
    for s in person:
        if s < M:
            ans = False
            break
        else:
            pain = (s//M)*K
            sell += 1
            pain -= sell
            if pain < 0:
                ans = False
    if ans:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')

