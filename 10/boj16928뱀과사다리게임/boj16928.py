import sys
from collections import deque
sys.stdin = open('input.txt')

# bfs 탐색 시, 카운트 횟수를 q에 가지고 다니면서 체크
# 튜플 타입일 경우 [1]의 값으로 q.append
# 다음에 간 곳이 100 (최종 목적지) 일 경우 cnt 값만 리턴
def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0] * 101
    visited[start] = 1
    while q:
        s, cnt = q.popleft()
        for next in range(1, 6+1):
            ns = s+next
            if 0 < ns <= 100:
                if not visited[ns]:
                    if type(board[ns]) == tuple:
                        visited[ns] = 1
                        q.append((board[ns][1], cnt+1))
                    else:
                        visited[ns] = 1
                        q.append((board[ns], cnt+1))
                    if ns == 100:
                        return q[-1][1]

# 사다리와 뱀이 실질적으로 2차원 형태에서 윗줄 아랫줄 이동이 아닌, 지정된 곳으로 이동이기에 1차원 배열로 받아도 무관
board = [t for t in range(101)]
N, M = map(int, sys.stdin.readline().split())

# 사다리로 갈 곳, 뱀으로 갈 곳은 튜플로 리스트에 저장 => 풀고보니 두가지 경우를 'L','S' 로 나눌 필요도 없었음
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    board[x] = ('L', y)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    board[u] = ('S', v)

print(bfs(board[1]))