import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(s, e):
    q = deque([s])
    visited[s] = 1
    while q:
        s = q.popleft()
        for i in famille[s]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[s] + 1                 # 촌 수 계산
            if i == e:                                      # 원하는 곳에 도착
                return visited[s]                           # 나랑 몇 촌 인지 이니까, 미포함 된 숫자
    return -1                                               # 없으면 -1


n = int(sys.stdin.readline())
s, e = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
famille = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    famille[x].append(y)
    famille[y].append(x)
# print(famille)

visited = [0] * (n+1)
print(bfs(s, e))