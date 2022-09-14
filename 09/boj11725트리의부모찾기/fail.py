import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(tree, start, end, visited):
    q = deque([start])                              # deque 설정
    visited[start] = True                           # 출발지 방문 처리
    while q:                                        # q가 빌 때 까지
        s = q.popleft()                             # 시작 지점
        for i in tree[s]:                           # 시작 노드와 연결 된 노드 중
            if visited[i] == 0:                     # 방문 이력이 없다면
                q.append(i)                         # 큐에 넣기
                visited[i] = False                  # 방문 처리
            if i == end:                            # 가려는 노드가 목표지점이라면
                return s                            # 현재 노드는 자식노드이므로 반환



N = int(sys.stdin.readline())                       # 노드의 개수

# 비어있는 트리 (1이 루트가 됨)
tree = [[] for _ in range(N+1)]
for _ in range(N-1):                                # N-1 개의 간선 표시
    x, y = map(int, sys.stdin.readline().split())
    tree[x].append(y)                               # 양방향 2차원 배열 생성
    tree[y].append(x)
# print(tree)

visited = [False] * (N+1)                           # 노드가 1부터 시작이므로, 방문처리 리스트 N+1개 만들어 줌
start = 1                                           # 시작 지점 / 루트 노트
for n in range(2, N+1):                             # 2번 노드부터 부모노드 체크
    end = n                                         # 2~N 까지 돌아가면서 목표지점으로 설정
    print(bfs(tree, start, end, visited))           # bfs 함수로 탐색



