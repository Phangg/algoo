import sys
sys.stdin = open('input.txt')

white_arr = [[0]*100 for _ in range(100)]

# 가로,세로 100 의 도화지 / 가로,세로 10의 색종이
# N : 색종이의 개수 / a, b : 색종이 왼쪽 하단의 좌표
N = int(sys.stdin.readline())
# 색종이 개수 * 10 * 10 (색종이 넓이)
all_area = N * 10 * 10

# x, y : 2차원 배열에서 인덱스로 비교하기 위해 미리 -1 해서 변수 저장
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    x = a - 1
    y = b - 1

# 색종이 범위에 1씩 더해주기 (중복 지역은 중복해서 더해줌)
    for i in range(0, 10):
        for j in range(0, 10):
            white_arr[x+i][y+j] += 1

# 중복지역 및 숫자 체크 -> 겹친 횟수이자 넓이 확인
overlap = 0
for i in range(100):
    for j in range(100):
        if white_arr[i][j] > 1:
            overlap += (white_arr[i][j] - 1)
            white_arr[i][j] = 1

print(all_area - overlap)