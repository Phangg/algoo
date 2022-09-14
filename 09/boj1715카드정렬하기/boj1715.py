import sys
import heapq
sys.stdin = open('input.txt')

N = int(input())
hq = []
for _ in range(N):
    heapq.heappush(hq, int(input()))
# print(hq)

ans = 0
while len(hq) > 1:
    a = heapq.heappop(hq)           # 최소 값 a 로 지정 (hq 에서 삭제 됨)
    b = heapq.heappop(hq)           # a가 사라진 뒤, 최소 값 b 로 지정 (hq 에서 삭제 됨)
    ans += (a + b)                  # a + b 값 저장
    heapq.heappush(hq, a + b)       # a + b 를 hq 에 삽입 (이 값을 포함해서 위 과정 반복)
print(ans)