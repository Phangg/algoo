import sys
import heapq
sys.stdin = open('39input.txt')
INF = int(1e9)

# 다익스트라 함수
def dij():
    hq = []
    si, sj = 0, 0                                           # 시작 포인트
    heapq.heappush(hq, (arr[si][sj], si, sj))               # 누적 값을 기준으로 최소 힙 구성
    dist[si][sj] = arr[si][sj]
    while hq:
        now_d, i, j = heapq.heappop(hq)
        if dist[i][j] < now_d:                              # 현재 위치의 누적 값이 더 크다? continue
            continue
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 델타 탐색
            ni, nj = i+di, j+dj
            if (0 <= ni < N) and (0 <= nj < N):
                cost = now_d + arr[ni][nj]                  # cost => 햔재 위치 누적값 + 갈 곳의 값
                if dist[ni][nj] > cost:                     # cost 가 더 작은 값이라면 바꿔주기
                    dist[ni][nj] = cost
                    heapq.heappush(hq, (cost, ni, nj))

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)]

    dij()
    print(dist[N-1][N-1])