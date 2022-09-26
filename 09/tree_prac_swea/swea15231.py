import sys
sys.stdin = open('15231input.txt')

def level_check(E):
    k = 0
    while (2 ** k) - 1 < E:
        k += 1
    return k

ans = []
T = int(input())
for tc in range(1, T+1):
    N, V = map(int, input().split())

    if V == 1:
        length = level_check(N) - 1
        ans.append(f'#{tc} {length}')
    else:
        length = (level_check(V) - 1) + (level_check(N) - 1)
        ans.append(f'#{tc} {length}')

for a in ans:
    print(a)
