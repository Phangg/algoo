import sys
sys.stdin = open('input.txt')

def prim(node):
    mst = [0]*(V+1)
    key = [float('inf')]*(V+1)
    parent = [-1]*(V+1)
    key[node] = 0
    for _ in range(V+1):
        min_val = float('inf')

        for i in range(V+1):
            if mst[i] == 0 and key[i] < min_val:
                idx = i
                min_val = key[i]
        mst[idx] = 1

        for e in range(V+1):
            if mst[e] == 0:
                for i in adj_lst[idx]:
                    if i[1] == e and key[e] > i[0]:
                        key[e] = i[0]
                        parent[e] = idx
    return sum(key)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_lst = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_lst[s].append([w, e])
        adj_lst[e].append([w, s])
    # print(adj_lst)
    print(f'#{tc} {prim(0)}')
