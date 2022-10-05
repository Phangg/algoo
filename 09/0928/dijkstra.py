'''
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''
from collections import defaultdict
V, E = map(int, input().split())
graph_di = defaultdict(list)
for _ in range(E):
    s, e, weight = map(int, input().split())
    graph_di[s].append((e, weight))
# print(graph_di)
    

def dijkstra(s):
    U = {s}
    distance = [float('inf') for _ in range(V+1)]
    distance[s] = 0

    for e, weight in graph_di[s]:
        distance[e] = weight

    for _ in range(V+1):
        min_val = float('inf')
        # idx = -1
        for i in range(V+1):
            if i not in U and min_val > distance[i]:
                min_val = distance[i]
                idx = i
        U.add(idx)

        for e, weight in graph_di[idx]:
            distance[e] = min(distance[e], distance[idx] + weight)
    print(distance)

dijkstra(1)


'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''

import heapq

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


V, E = map(int, input().split())
start = int(input())
adj_lst = [[] * (V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_lst[u].append((w, v))

x = dij(start)
print(x)