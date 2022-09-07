# 너비 우선 탐색
# 큐 자료구조를 이용하는 것이 정석
# deque 라이브러리 사용

# 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다
# 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 가능할 때까지 반복
from collections import deque

def bfs(graph, s, visited):
    q = deque([s])
    visited[s] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)