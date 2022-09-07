import sys
sys.stdin = open('input.txt')

# 우 좌 상  (밑에서부터 올라가니, 아래 방향 없이)
di = [0, 0, -1]  # 행
dj = [1, -1, 0]  # 열

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    x, y = 99, 0   # 스타트 좌표 (밑에서 부터 출발 위해, y 변경 예정)
    for i in range(100):
        if arr[-1][i] == 2:
            y = i    # y 에 맨 밑 행에서 2가 있는 인덱스 값 넣어주기
    # y = lst[-1].index(2)

    while x > 0:   # 0 행에 도달할 때까지
        for d in range(3):
            nx = x + di[d]
            ny = y + dj[d]
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1:   # 박스 밖으로 나가지 않게 제한
                arr[x][y] = 0  # 이미 지나간 길 체크
                x = nx
                y = ny

    print(f'#{tc} {y}')


