import sys
sys.stdin = open('input.txt')

N, M, B = map(int, sys.stdin.readline().split())
# land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(land)
land = []
for _ in range(N):
    land.extend(list(map(int, sys.stdin.readline().split())))
# print(land)

maxxx = (sum(land) + B) // (N * M)
if maxxx > 256:
    maxxx = 256

time = []
for i in range(maxxx+1):    # i : 목표
    mx, mn = 0, 0
    for j in land:          # j : 땅의 높이
        if i > j:           # 목표보다 낮을 때
            mn += (i-j)     # mn 만큼 블록 채우기
        elif i < j:         # 목표보다 높을 때
            mx += (j-i)     # mx 만큼 블록 없애기

    inven = mx + B          # 총 블록 수

    if inven < mn:          # 블럭 부족? => 넘기기
        continue

    time.append([(mx * 2) + mn, i])

time.sort(key=lambda x: (x[0], -x[1]))
# print(time)
print(*time[0])
