import sys
import heapq
sys.stdin = open('input.txt')

def dij(node):
    dist = [float('inf')] * (V+1)
    dist[node] = 0
    hq = []
    heapq.heappush(hq, [0, node])

    while hq:
        now_w, now_v = heapq.heappop(hq)
        for w, v in adj_lst[now_v]:
            w += now_w
            if w < dist[v]:
                dist[v] = w
                heapq.heappush(hq, [w, v])
    return dist


V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
adj_lst = [[] * (V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    adj_lst[u].append((w, v))

x = dij(start)
# print(x)

for t in range(1, len(x)):
    if x[t] != float('inf'):
        print(x[t])
    else:
        print('INF')