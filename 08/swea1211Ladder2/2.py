import sys
sys.stdin = open('input.txt')

def start_point(ladder, N):                 # 시작점 여러개 -> 리스트에 저장 함수
    lst = []
    for n in range(N):
        if ladder[0][n] == 1:
            lst.append(n)
    return lst

def way_check(ladder, N, s):                # 한 시작점에서 도착지까지 이동하는 경로 길이
    #     우 좌 하
    di = [0, 0, 1]
    dj = [1, -1, 0]

    visited = [[0] * N for _ in range(N)]
    x, y = 0, s
    way_cnt = 0
    while x < N-1:
        visited[x][y] = 1
        for d in range(3):
            nx = x + di[d]
            ny = y + dj[d]
            if (0 <= nx < 100) and (0 <= ny < 100) and (ladder[nx][ny] == 1) and (visited[nx][ny] != 1):
                way_cnt += 1
                x = nx
                y = ny
                break
    return way_cnt

T = 10
N = 100
for _ in range(T):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]

    start_lst = start_point(ladder, N)                          # 시작점의 인덱스 (위치)

    ans_lst = []
    for s in start_lst:
        ans_lst.append(way_check(ladder, N, s))                 # 각 시작지점마다 도착지 이동 시간을 ans_lst 에 저장

    ans = ans_lst.index(min(ans_lst))                           # ans_lst 의 최소값 = 가장 적게 걸리는 경로 -> ans_lst 에서 몇번째?
    print(f'#{tc}', start_lst[ans])                             # start_lst 인덱스 순서 == ans_lst 인덱스 순서 -> start_lst는 전체 배열에서의 인덱스 값 -> 출력