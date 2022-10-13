# pypy3 통과 / python3 시간초과

import sys
from itertools import permutations
sys.stdin = open('input.txt')

def problem():
    global max_v, min_v
    for x in permutations(op, N-1):                 # 연산자 조합이 나올 수 있는 경우들을 순회 / x : 조합
        res = A[0]                                  # 결과 값 : 초기 설정 -> 첫 값
        for k in range(1, N):                       # 첫 값이 이미 들어갔으니, 1부터 순회
            if x[k-1] == '+':
                res += A[k]
            elif x[k-1] == '-':
                res -= A[k]
            elif x[k - 1] == '*':
                res *= A[k]
            elif x[k-1] == '/':
                res = int(res / A[k])
        if res > max_v:
            max_v = res
        if res < min_v:
            min_v = res


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
op = []

# 연산자 개수 별로 op 리스트에 넣기
for i, o in enumerate(op_num):
    for j in range(o):
        op.append(op_list[i])
# print(op)

max_v = -1000000001
min_v = 1000000001

problem()

print(max_v)
print(min_v)

