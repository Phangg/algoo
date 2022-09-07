import sys
sys.stdin = open('input.txt')

# i : 인덱스 , N : 전체 인원 , n : 한팀 인원 , a : a팀, b: b팀
def team(i, N, n, a, b):
    global lst
    if i == n:
        # print(a,b)
        sum_a = 0
        sum_b = 0
        for x in range(n):
            for y in range(x, n):                       # x, y 같은 경우 필요 없음
                nx = a[x]
                ny = a[y]
                sum_a += S[nx][ny] + S[ny][nx]          # a에 여러개 인덱스 있을 때, 모든 경우 다 더해주기
        for x in range(n):
            for y in range(x, n):                       # b 도 마찬가지
                nx = b[x]
                ny = b[y]
                sum_b += S[nx][ny] + S[ny][nx]
        # print(sum_a, sum_b)
        gap = abs(sum_a - sum_b)                        # 두 팀 점수의 차이
        lst.append(gap)                                 # global 선언 된 리스트에 담아주기
        return

    x = 0                                               # 중복 피하는 조합으로 만들기
    if a:
        x = max(a) + 1

    for j in range(x, N):                               # 중복 피하는 조합으로 만들기
        if j not in a:
            a.append(j)
            if a[0] != 0:                               # a 리스트 맨 앞에 0으로 오는 것들만 체크하면, a,b 중복 처리 가능
                break
            if len(a) == n:                             # a 길이가 채워졌을 때,
                for k in range(N):
                    if k not in a and k not in b:       # b 만들기
                        b.append(k)
            team(i+1, N, n, a, b)
            a.pop()
            b.clear()                                   # a pop 할때, b도 완전 새로 할당 받아야하니까 비워주기

# N : 모인 인원 (짝수)
N = int(sys.stdin.readline())
# 한팀은 N/2 명
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(S)

lst = []
a = []
b = []
team(0, N, N//2, a, b)
# print(lst)

print(min(lst))                                         # a, b 팀의 점수 차이가 들어있는 리스트에서 최소값 출력