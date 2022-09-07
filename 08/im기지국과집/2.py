import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = 3
for tc in range(1, T+1):
    N = int(input())
    M = 10
    MAP = [list(input()) for _ in range(M)]

    len_dict = {'A': 1, 'B': 2, 'C': 3}

    for r in range(M):
        for c in range(N):
            if MAP[r][c] == 'X' or MAP[r][c] == 'H':
                continue
            # K = 0
            # if MAP[r][c] == 'A': K = 1
            # elif MAP[r][c] == 'B': K = 2
            # else: K = 3
            K = len_dict[MAP[r][c]]

            for i in range(4):
                for j in range(1, K + 1):
                    nr = r + dr[i] * j
                    nc = c + dc[i] * j
                    if nr < 0 or nr >= N or nc < 0 or nc >= N:
                        break
                    if MAP[nr][nc] == 'H':
                        MAP[nr][nc] = 'X'

    ans = 0
    for r in range(M):
        for c in range(N):
            if MAP[r][c] == 'H':
                ans += 1

    print(ans)

    # for line in MAP:
        # print(line)