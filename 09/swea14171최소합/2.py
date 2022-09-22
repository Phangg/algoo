def dfs(r, c):
    visited = [[0] * n for _ in range(n)]
    visited[r][c] = square[r][c]
    stack = []
    stack.append((r, c))
    s = 10 * n * n
    while stack:
        r, c = stack[-1]
        if r == n - 1 and c == n - 1:
            now = visited[r][c]
            s = min(s, now)
        dr = [0, 1]
        dc = [1, 0]
        for k in range(2):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                tmp = visited[r][c] + square[nr][nc]
                if visited[nr][nc] == 0 or visited[nr][nc] > tmp:
                    stack.append((nr, nc))
                    visited[nr][nc] = tmp
                    break
        else:
            stack.pop()
    return s


t = int(input())
for tc in range(t):
    n = int(input())
    square = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc + 1} {dfs(0, 0)}')
