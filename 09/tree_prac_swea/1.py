from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if graph.get(now):
            for next in graph[now]:
                q.append(next)
        else:
            cnt += 1

n = int(input())
p = list(map(int, input().split()))
del_node = int(input())
graph = {}
for i, v in enumerate(p):
    if v in graph:
        graph[v].append(i)
    else:
        graph[v] = [i]
print(graph)

# 노드 삭제하기
del_parent = p[del_node]
if del_parent == -1:     # 루트를 삭제할 경우
    print(0)
else:
    graph[del_parent].remove(del_node)
    cnt = 0
    bfs(p.index(-1))
    print(cnt)