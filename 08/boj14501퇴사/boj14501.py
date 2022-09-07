import sys
sys.stdin = open('input.txt')

N = int(input())
T_lst = []
P_lst = []
for _ in range(N):
    T, P = map(int, input().split())
    T_lst.append(T)
    P_lst.append(P)                                                   # T 기간 / P 금액  각각 리스트 생성 및 값 입력

max_p = [0] * (N + 1)
for i in range(N-1, -1, -1):                                          # 뒤에서부터 들어갈 수 있는 가장 큰 값 넣어주기.
    if T_lst[i] + i > N:                                              # 당일도 상담일에 포함이라, N과 같아도 괜찮다.
        max_p[i] = max_p[i + 1]
    else:
        max_p[i] = max(P_lst[i] + max_p[i + T_lst[i]], max_p[i + 1])  # P_lst[i] + max_p[i + T_lst[i]] -> 이거 상담하면 받는 금액 + 상담 못하는 기간 이후에 내가 갖고 있는 금액
                                                                      # max_p[i + 1] -> 이 상담 안했을 때 가지고 있는 금액
print(max_p[0])                                                       # 0번 인덱스의 값이 최대 값을 가짐




