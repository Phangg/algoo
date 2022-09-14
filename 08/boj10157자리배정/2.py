import sys
from pprint import pprint
sys.stdin = open('input.txt')

def check(lst, r, c, k):
    for i in range(r):                  # 행
        for j in range(c):              # 열
            if lst[i][j] == k:
                return j+1, (r - i)         # 0,0 이 1,1 로 나타나니깐 +1 / x 좌표는 뒤집혀있으니 행 - i 출력
    return 0

# C : 공연장 가로 / R : 공연장 세로 / K : 관객 대기번호
C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

# 공연장에 1 ~ c*r까지 숫자를 배정할 예정으로 숫자 리스트 생성
num_lst = list(range(1, (C*R)+1))

if C*R < K:                                                     # K가 크면 일단 땡
    res = 0
else:                                                           # K 가 범위 안에 있으면 밑에 진행
    ans = [[0] * C for _ in range(R)]

    x, y = R, 0
    num = 0
    xxx = 0                                                     # 브레이크 용 변수
    while num < K:
        for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            if xxx == 1:
                break
            while 1:
                nx, ny = x+di, y+dj
                if (0 <= nx < R) and (0 <= ny < C) and ans[nx][ny] == 0:
                    num += 1
                    ans[nx][ny] = num
                    x, y = nx, ny
                    if num == K:                                # K 만나면 그만 돌아도 돼
                        xxx = 1
                        break
                else:
                    break
    # pprint(ans)

    res = check(ans, R, C, K)
if res:
    print(*res)                         # res 값 있을 때 -> 출력
else:
    print(res)                          # res 0 -> 출력