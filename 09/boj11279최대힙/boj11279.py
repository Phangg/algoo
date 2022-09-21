import sys
import heapq
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(hq, (-x, x))     # heapq 는 디폴트가 최소힙
    else:                               # -x, x 튜플로 넣어서 최대힙 모양 구성
        if len(hq):
            ans = heapq.heappop(hq)[1]
            print(ans)
        else:
            print(0)