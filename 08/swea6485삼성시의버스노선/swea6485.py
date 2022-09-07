import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ab_lst = []
    for _ in range(N):
        A, B = map(int, input().split())
        ab_lst.append([A, B])                               # [A,B] 로 된 2차원 배열
    # print(ab_lst)
    P = int(input())
    c_lst = [int(input()) for _ in range(P)]                # c / 정류장 번호 리스트 저장
    # print(c_lst)

    ans_lst = [0] * 5001                                    # 문제에서 5000개의 정류장 제시 / idx 와 정류장 번호 차이로 5001까지 지정

    for i in range(N):
        for j in range(ab_lst[i][0], ab_lst[i][-1]+1):      # 1번 버스 1~3 / 2번 버스 2~5 값 j로 빼기
            ans_lst[j] += 1                                 # ans_lst(정류장 리스트)에 버스들이 지나치는 횟수 저장

    res = []
    for c in c_lst:
        res.append(ans_lst[c])
    print(f'#{tc}', *res)