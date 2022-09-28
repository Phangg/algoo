import sys
sys.stdin = open('1795input.txt')

def dij(N, X, adj, d):
    for i in range(N+1):
        d[i] = adj[X][i]

    U = [x]
    for _ in range(N-1):        # N개의 정점 중 출발을 제외한 정점 선택
        w = 0
        for i in range(1, N+1):
            if i not in U and d[i] < d[w]:      # 남은 노드 중 비용이 최소인 w
                w = i
        U.append(w)
        for v in range(1, N+1):                 # 정점 i가
            if 0 < adj[w][v] < 1000000:        # i가 w에 인접이면
                d[v] = min(d[v], d[w] + adj[w][v])


T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())

    adj_m = [[1000000] * (N+1) for _ in range(N+1)]
    re_adj_m = [[1000000] * (N+1) for _ in range(N+1)]
    for i in range(N-1):
        adj_m[i][i] = 0
        re_adj_m[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj_m[x][y] = c
        re_adj_m[y][x] = c

    d_out = [0] * (N+1)
    d_in = [0] * (N+1)
    dij(N, X, adj_m, d_out)
    dij(N, X, re_adj_m, d_in)
    # print(d_out)
    # print(d_in)
    ans = 0
    for l in range(1, N+1):
        tmp = d_out[l] + d_in[l]
        if ans < tmp:
            ans = tmp
    print(f'#{tc} {ans}')