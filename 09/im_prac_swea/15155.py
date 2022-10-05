import sys
sys.stdin = open('15155input.txt')

def check(arr):
    for i in range(N):
        for j in range(N):
            for di, dj in [[0, 1], [1, 0], [-1, 1], [1, 1]]:
                for k in range(5):
                    ni, nj = i+di*k, j+dj*k
                    if (0 > ni) or (ni >= N) or (0 > nj) or (nj >= N) or (arr[ni][nj] != 'o'):
                        break
                else:
                    return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    omok = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    print(f'#{tc}', check(omok))
