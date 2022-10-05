import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(s):
    q = deque()
    visited = [0] * (N+1)
    q.append(s)
    visited[s] = 1
    while q:
        x = q.popleft()
        for next in cross_line[x]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[x] + 1
                if end in stop_station_line[next]:
                    return visited[next] - 1
    return float('inf')

# 인풋 받기
N = int(sys.stdin.readline())

# 각 호선 별로 정차하는 역을 담을 리스트
stop_station_line = [[] for _ in range(N+1)]
# 각 호선 별로 환승이 가능한 호선을 담을 리스트
cross_line = [[] for _ in range(N+1)]

for n in range(1, N+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for x in range(1, len(tmp)):
        stop_station_line[n].append(tmp[x])
# 종점
end = int(sys.stdin.readline())

# 1호선에서 갈수 있는 호선을 체크해서 cross_line 리스트에 양방향으로 넣어주기
for i in range(1, N+1):
    for j in range(len(stop_station_line[i])):
        for p in range(i+1, N+1):
            for q in range(len(stop_station_line[p])):
                if stop_station_line[i][j] == stop_station_line[p][q]:
                    cross_line[i].append(p)
                    cross_line[p].append(i)

# 2차원 배열 stop_station_line 에서 각 호선별로 0 (시작점:서울역) 이 있는지 체크 => bfs GO!!
min_v = float('inf')
flag = 0
for idx, lst in enumerate(stop_station_line):
    if 0 in lst:
        if end in lst:      # 근데 출발지랑 도착지랑 같은 호선? print(0) 을 위해 flag 세우기
            flag = 1
            break
        else:
            v = bfs(idx)    # 0 (출발지) 만 있으면 함수 GO
            if min_v > v:   # 함수 돌고 나와서 최소 값 체크
                min_v = v
if flag:
    print(0)
elif min_v == float('inf'):
    print(-1)               # 함수 돌고 나왔는데 'inf' ? -> 도착지 못가는 상태임
else:
    print(min_v)