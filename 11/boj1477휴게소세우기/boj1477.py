import sys
sys.stdin = open('input.txt')

n, m, L = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.append(0)
lst.append(L)
lst.sort()

# 각 지점의 거리가 담긴 리스트
dist = []
for x in range(0, n+1):
    dist.append(lst[x+1]-lst[x])

ans = 0
s, e = 1, L
while s <= e:
    cnt = 0
    mid = (s + e) // 2
    for d in dist:
        # 현재 거리 중 mid 보다 큰 거리 찾기
        if d > mid:
            # 현재 설치 구역 제외 => -1 / mid 로 나누어지는 만큼 설치
            cnt += (d - 1) // mid
    if cnt > m:
        s = mid + 1
    else:
        e = mid - 1
        ans = mid

print(ans)