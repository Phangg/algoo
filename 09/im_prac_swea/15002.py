import sys
sys.stdin = open('15002input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    s = 0
    x = N//2
    i = 0
    tmp = 1
    for lst in arr:
        if tmp:
            s += sum(lst[x-i:x+i+1])
            if x+i+1 == N:
                tmp = 0
                continue
            i += 1
        else:
            i -= 1
            s += sum(lst[x-i:x+i+1])
            if not i:
                break
    print(f'#{tc} {s}')
