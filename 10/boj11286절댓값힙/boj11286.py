import sys
import heapq
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)