import sys
sys.stdin = open('input.txt')

# 우 하 좌 상 순서 -> 달팽이 회전 순서
di = [0, 1, 0, -1]  # 행
dj = [1, 0, -1, 0]  # 열

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [[0] * N for _ in range(N)]

    x, y = 0, 0  # 초기 스타팅 위치
    d = 0  # 첫번째는 진행 방향이 우측 -> di, dj 의 0번 인덱스 참조 예정
    for s in range(1, N*N+1):  # 1부터 N*N 까지 순서대로 2차 배열에 삽입 예정
        lst[x][y] = s  # 0,0=1 / 0,1=2 / 0,3=3 / ...
        x += di[d]
        y += dj[d]
        if y >= N or x >= N or y < 0 or x < 0 or lst[x][y] != 0:
            # 각 라인 끝에 닿을 경우 (처음 한바퀴) / 이미 각 요소가 0 으로 채워져 있으니, 다른 숫자를 만났을 때 진행
            x -= di[d]  # 이미 한번 지나치면서 if 문에 검색된 것이기 때문에 한번 지워주기
            y -= dj[d]

            d = (d + 1) % 4  # 처음 d는 0 / 이제 부터 0,1,2,3 반복
            x += di[d]
            y += dj[d]

    print(f'#{tc}')
    for n_lst in lst:
        for n in n_lst:
            print(n, end=' ')
        print()

