import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(s, g, V):
    visited = [0] * (V+1)                       # 노드가 1부터 시작하기에 +1
    q = deque()
    q.append(s)                                 # 시작점 추가
    visited[s] = 1                              # 시작점 방문 체크

    while q:                                    # q가 다 빌 때 까지
        p = q.popleft()                         # p 에 popleft 값 저장
        for i in lst[p]:                        # p 노드에 연결 된 노드 확인
            if visited[i] == 0:                 # 방문 기록 없으면
                q.append(i)                     # q 에 추가 / 방문
                visited[i] = visited[p] + 1     # 이전 노드 숫자 +1
            if i == g:                          # 도착점이라면
                return visited[i] - 1           # 도착 할 때 값이니까 -1
    return 0                                    # 도착 못하는 경우



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        lst[start].append(end)
        lst[end].append(start)
    s, g = map(int, input().split())
    # print(lst)

    print(f'#{tc}', bfs(s, g, V))

