import sys
sys.stdin = open('input.txt')
INF = int(1e9)

# n : 도시의 개수 / m : 버스의 개수
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF] * (n+1) for _ in range(n+1)]

# a에서 b로 가는 가중치를 그래프에 넣기 / 기존 입력 값보다 c가 작을 때 입력!!
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] > c:
        graph[a][b] = c

# 시작 도시와 도착 도시가 같은 경우는 없음
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 거쳐가는 것이 더 빠르다면 값 대체
for k in range(1, n+1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력
for i in range(1, n+1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()