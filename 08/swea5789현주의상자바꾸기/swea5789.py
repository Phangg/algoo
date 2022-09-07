import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())                        # N 개의 상자 / Q 회 반복
    # print(N, Q)
    ans_lst = [0] * (N+1)
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            ans_lst[j] = i+1

    ans_lst = ans_lst[1:]                                   # 리스트 0번 인덱스 의미 없으니, 리스트 재정의
    print(f'#{tc}', *ans_lst)