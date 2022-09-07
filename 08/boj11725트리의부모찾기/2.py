import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                       # 노드의 개수

# 비어있는 트리 (1이 루트가 됨)
tree = [[] for _ in range(N+1)]

for _ in range(N-1):                                # N-1 개의 간선 표시
    x, y = map(int, sys.stdin.readline().split())
    tree[x].append(y)                               # 양방향 2차원 배열 생성
    tree[y].append(x)
# print(tree)
visited = [False] * (N+1)                           # 방문 처리를 위한 리스트 / 노드가 1부터 시작이라 N+1 로 만듦
ans = [0] * (N+1)                                   # 부모 노드를 저장 할 리스트

q = deque([1])                                      # 시작 노드 1 - 루트 노드
visited[1] = True                                   # 시작 노드 1 - 루트 노드

while q:
    s = q.popleft()                                 # 노드의 밑으로 연결된 자식 노드 파악
    for i in tree[s]:                               # 노드에 연결 된 인접 노드 체크
        if visited[i] == False:                     # 방문 이력 없다면
            q.append(i)                             # 큐에 추가
            visited[i] = True                       # 방문 처리
            ans[i] = s                              # 루트 노드 부터 시작한 탐색으로, 부모노드 저장

for x in ans[2:]:                                   # 2번 노드부터 출력
    print(x)