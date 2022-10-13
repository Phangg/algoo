import sys
import heapq
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
hq = []
max_hq = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if len(max_hq) == len(hq):
        heapq.heappush(max_hq, (-x, x))
    else:
        heapq.heappush(hq, x)

    if hq and hq[0] < max_hq[0][1]:
        a = heapq.heappop(hq)
        b = heapq.heappop(max_hq)[1]
        heapq.heappush(hq, b)
        heapq.heappush(max_hq, (-a, a))

    # print(hq)
    # print(max_hq)

    print(max_hq[0][1])

