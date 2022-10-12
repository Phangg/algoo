# 플로이드 워셜 알고리즘

# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용
# 단계마다 '거쳐 가는 노드' 를 기준으로 알고리즘 실행
# (다익스트라 와 달리 매번 미방문 노드 중 최단 거리 노드 찾을 필요 X)
# 노드의 개수가 N 개일 때, N번의 단계를 수행 / 단계마다 O(N^2)의 연산 => 총 시간 복잡도 O(N^3)
# why? => 2차원 리스트에 최단 거리 정보를 저장
# DP.... => 노드의 개수만큼 '점화식' 에 맞게 2차원 리스트를 갱신....
# 점화식 => DP(a,b) = min(DP(a,b), DP(ak)+DP(kb))
# (A에서 B로 가는 최소 비용, A에서 K를 거쳐 B로 가는 비용) 을 비교하는 것

INF = int(1e9)

# n : node / m : line
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# a 노드에서 b 노드로 가는 가중치는 c
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# a에서 b를 갈 때, k를 지나쳐서 가는 것이 더 빠른지 체크
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 바뀐 그래프의 값을 확인해서 출력하기
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print('INFINITY')
            break
        else:
            print(graph[a][b], end=' ')
    print()

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''