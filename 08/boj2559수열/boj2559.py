import sys
sys.stdin = open('input.txt')

def min_temp(x: list, n, k):                    # 시간 초과로 인해 최대한 연산 적게 해보려고 함
    max_t = sum(x[:k])                          # max 값에 첫번째 값 넣어두고 그때그때 비교해서 max 값 가지기 / 처음엔 리스트에 넣고 마지막에 max함수로 뽑았었음
    s = sum(x[:k])                              # 첫번째 합을 변수에 저장하고 시작
    for i in range(n - k):
        s = s - (x[i]) + (x[i+k])               # 첫번째 합 s 에서 맨 앞에 값 빼고, 맨 뒤에 값 넣어주기만 하면 새로운 값(합)을 가질 수 있음
        if max_t < s:                           # max값 비교해서 저장
            max_t = s
    return max_t

# N : 전체 날짜 수 / K : 연속적인 날짜 수 / temp_lst : N일간 온도 리스트 (N개의 숫자)
N, K = map(int, sys.stdin.readline().split())
temp_lst = list(map(int, sys.stdin.readline().split()))

print(min_temp(temp_lst, N, K))