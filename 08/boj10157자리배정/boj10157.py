import sys
from pprint import pprint
sys.stdin = open('input.txt')

def check(lst, r, c, k):
    for i in range(r):                  # 행
        for j in range(c):              # 열
            if lst[i][j] == k:
                return j+1, i+1         # 0,0 이 1,1 로 나타나니깐 +1 해서 출력
    return 0


# 옆으로 돌아간 형태로 사실상 세로 가로 바뀐 상태
# 0,0 => 1,1 로 표시되기에 출력시 +1 필요

#     우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# C : 공연장 가로 / R : 공연장 세로 / K : 관객 대기번호
C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

# 비어있는 공연장 생성
# 가로 세로 바뀐 것과 동일 => C 세로 / R 가로로 만들기
stage = [[0]*R for _ in range(C)]

# 공연장에 1 ~ c*r까지 숫자를 배정할 예정으로 숫자 리스트 생성
num_lst = list(range(1, (C*R)+1))

# x, y => 출발지점 / d => di,dj 리스트의 인덱스 (방향 조정을 위해 사용)
x, y = 0, -1
d = 0

for num in num_lst:
    nx = x + di[d]
    ny = y + dj[d]
    if (0 <= nx < C) and (0 <= ny < R) and stage[nx][ny] == 0:
        stage[nx][ny] = num             # stage 범위 내에 있고, 다음 자리 비었을 때, 추가
        x = nx
        y = ny
    else:
        nx -= di[d]                     # 이미 nx,ny 는 범위를 벗어남
        ny -= dj[d]                     # 다시 하나 뒤로 돌아가서 범위 내에 위치
        d = (d+1) % 4                   # 방향 조정
        x = nx + di[d]
        y = ny + dj[d]
        stage[x][y] = num               # 추가
# pprint(stage)

res = list(map(list, zip(*stage)))
# pprint(res)
ans = check(res, R, C, K)   # 위에서 K가 있는 해당 좌표 함수 이용
if ans:
    print(*ans)             # ans 0 -> 요소만 출력
else:
    print(ans)              # ans 0 -> 출력