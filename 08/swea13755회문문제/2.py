import sys
sys.stdin = open('input.txt')

def palin(n, m, lst):
    for x in lst:
        for y in range(n-m+1):
            asd = ''
            dsa = ''
            for z in range(m):
                asd += x[y+z]
            for v in range(m-1, -1, -1):
                dsa += x[y+v]
            if asd == dsa:
                return asd

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    arr_h = list(map(list, zip(*arr)))

    i = palin(N, M, arr)
    j = palin(N, M, arr_h)

    if i == None:
        print(f'#{tc} {j}')
    else:
        print(f'#{tc} {i}')