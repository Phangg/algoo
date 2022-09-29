# 시간 초과....

import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def dij(node):
    dist = [float('inf')] * (V+1)
    dist[node] = 0
    visited = set()
    visited.add(node)

    for e, w in graph_dict[node]:
        dist[e] = w

    for _ in range(V+1):
        min_v = float('inf')
        for i in range(V+1):
            if i not in visited and dist[i] < min_v:
                idx = i
                min_v = dist[i]
        visited.add(idx)

        for e, w in graph_dict[idx]:
            dist[e] = min(dist[e], dist[idx] + w)
    return dist


V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
graph_dict = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph_dict[u].append([v, w])

x = dij(start)
# print(x)

for t in range(1, len(x)):
    if x[t] != float('inf'):
        print(x[t])
    else:
        print('INF')