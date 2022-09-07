import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())             # N*N 영역 / M*M 파리채 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_d = 0                                    # 가장 많이 죽은 파리의 수
    for i in range(N-M+1):                       # i 행
        for j in range(N-M+1):                   # j 열
            area = 0                             # 파리채가 닿는 면적
            for k in range(j, M+j):              # 파리채가 2일때, 0,0 / 0,1 의 값을 면적에 더해줌
                area += arr[i][k]
                for n in range(i+1, M+i):        # 1,0 / 1,1 의 값을 면적에 더해줌
                    area += arr[n][k]
            if area > max_d:                     # 파리채로 때린 곳에서 죽을 파리의 수가 max_d 변수 값보다 클때
                max_d = area
    print(f'#{tc} {max_d}')
