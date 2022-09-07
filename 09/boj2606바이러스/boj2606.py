import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(s):
    ans = []                            # 바이러스 전염된 컴퓨터 리스트 (1번 본인 제외)
    q = deque([s])
    visited[s] = 1
    while q:
        s = q.popleft()
        for i in com[s]:
            if visited[i] == 0:
                q.append(i)
                ans.append(i)
                visited[i] = 1
    return len(ans)                     # 몇개?


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
com = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    com[x].append(y)
    com[y].append(x)
# print(com)

visited = [0] * (N+1)
s = 1
print(bfs(s))