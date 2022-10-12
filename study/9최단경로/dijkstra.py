'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        now_d, now_n = heapq.heappop(q)
        if dist[now_n] < now_d:
            continue
        for next_n, next_d in graph[now_n]:     # graph => (b,c) 중에  c 에 가중치 저장이기 때문
            cost = next_d + now_d
            if cost < dist[next_n]:
                dist[next_n] = cost
                heapq.heappush(q, (cost, next_n))

# n : node / m : line
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))                     # a: start node / b: end node / c: distance
# print(graph)

dijkstra(start)

for i in range(1, n+1):
    if dist[i] == INF:
        print('INFINITY')
    else:
        print(dist[i])