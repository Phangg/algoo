import sys
sys.stdin = open('input.txt')

# def minnn(A, B):
#     b = B.pop(B.index(max(B)))
#     a = A.pop(A.index(min(A)))
#     return a * b
#
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
#
# X = A[:]
# Y = B[:]
# ans = 0
# while len(X) > 0:
#     ans += minnn(X, Y)
# print(ans)

s = 0
for i in range(N):
    s += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))
print(s)