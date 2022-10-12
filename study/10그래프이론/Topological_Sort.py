# 위상 정렬

# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘
# 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열 하는 것'
# ex) 선수과목을 고려한 학습 순서 설정 등....
# '진입 차수 Indegree' => 특정한 노드로 들어오는 간선의 개수
# 진입 차수가 0 인 노드를 큐에 넣기 => 큐가 빌 때까지 다음 두가지 과정 반복
# ( 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거 )
# ( 새롭게 진입차수가 0이 된 노드를 큐에 넣기 )
# 위 과정을 통해, 원소의 개수만큼 큐에서 추출되기 전에 큐가 비어버린다면 사이클이 발생한 것을 알 수 있음
# 시간복잡도 : O(V+E) => 노드와 간선을 모두 확인하는 것

'''
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
'''

from collections import deque

def topology_sort():
    q = deque()
    res = []
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        res.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    print(*res)


v, e = map(int, input().split())
# 진입차수 모두 0으로 잡고 시작
indegree = [0] * (v+1)
# 연결 리스트 초기화
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # b 에 진입차수 +1 해주기
    indegree[b] += 1

topology_sort()