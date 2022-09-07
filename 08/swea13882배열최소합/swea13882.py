import sys
sys.stdin = open('input.txt')

# 중복 없이 순열 만들기
def p(i, N):
    global minsum                           # global 선언
    if sum(res[:i]) > minsum:               # 최소값보다 큰 숫자들이 있다면 하지 말아라
        return
    if i == N:                              # i = N
        if minsum > sum(res[:N]):           # 한 순열의 합 과 최소값 비교
            minsum = sum(res[:N])
        return
    for n in range(N):
        if n not in x[:i]:
            x[i] = n                        # 인덱스 순열 생성
            res[i] = lst[i][n]              # 2차원 배열에서 해당되는 인덱스 값을 res리스트에 삽입
            p(i+1, N)                       # 재귀


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]


    minsum = N * 10                         # 최소 sum -> 숫자는 10보다 작은 자연수
    res = [0] * N                           # 한 순열의 합을 구하기 위한 리스트
    x = [0] * N                             # 한 순열에 들어갈 인덱스를 구하기 위한 리스트
    p(0, N)
    print(f'#{tc} {minsum}')