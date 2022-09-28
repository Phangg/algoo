'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

V, E = map(int, input().split())
adj_m = [[0] * (V+1) for _ in range(V+1)]
adj_l = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())     # w : 가중치
    adj_m[u][v] = w
    adj_m[v][u] = w
    adj_l[u].append((v, w))
    adj_l[v].append((u, w))
print(adj_m)
print(adj_l)