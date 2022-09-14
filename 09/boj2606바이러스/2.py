import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(s):
    cnt = 0                                     # 몇개의 컴퓨터를 지나가는지 체크
    visited[s] = 1                              # 지나감 체크
    q = deque([s])                              # 시작 지점
    while q:
        s = q.popleft()
        for i in arr[s]:
            if visited[i] == 0:
                visited[i] = 1                  # 지나감 체크
                q.append(i)
                cnt += 1                        # 카운팅
    return cnt



com = int(sys.stdin.readline())
line = int(sys.stdin.readline())
arr = [[] for _ in range(com+1)]                    # 1번 컴퓨터부터 시작 -> com+1 개 리스트
for _ in range(line):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)                                # 양방향으로 연결된 배열로 만들어 주기
    arr[y].append(x)
# print(arr)
visited = [0] * (com+1)
start = 1
print(bfs(start))
