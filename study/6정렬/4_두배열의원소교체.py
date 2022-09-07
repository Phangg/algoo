import sys
sys.stdin = open('4input.txt')

# N : 배열 길이(원소 개수) / K : 교체 회수 / A 리스트 / B 리스트
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for i in range(K):
    A.append(B.pop())

for i in range(K):
    B.append(A.pop(0))

print(sum(A))