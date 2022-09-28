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

    x = level_check(N) - 1
    if V == 1:
        length = x
        ans.append(f'#{tc} {length}')
    else:
        y = (level_check(V) - 1)

        # N이 왼쪽에서 끝나고, V도 왼쪽에서 시작할 경우 => 레벨로 확인하기 때문에 -1 해주면 된다.
        # 완전 이진트리 이기 때문에 가능한 꼼수..?
        if V < (2**(y+1) - 1) - (((2**y)-1)//2) and N < (2**(x+1) - 1) - (((2**x)-1)//2):
            length = y + x - 1
            ans.append(f'#{tc} {length}')
        else:
            length = y + x
            ans.append(f'#{tc} {length}')

for a in ans:
    print(a)
