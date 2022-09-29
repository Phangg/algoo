###### prim #######

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

from collections import defaultdict
import heapq


def prim2(node):
    mst = []

    visited = {node}

    candidate = graph_list[node]
    heapq.heapify(candidate)

    while len(visited) <= V and candidate:
        weight, s, e = heapq.heappop(candidate)

        if e not in visited:
            visited.add(e)
            mst.append((weight, s, e))

            for route in graph_list[e]:
                if route[2] not in visited:
                    heapq.heappush(candidate, route)

    return sum(map(lambda x: x[0], mst))


V, E = map(int, input().split())
graph_list = defaultdict(list)

for _ in range(E):
    s, e, weight = map(int, input().split())
    graph_list[s].append((weight, s, e))
    graph_list[e].append((weight, e, s))

# print(graph_list)
ans = prim2(0)
print(ans)