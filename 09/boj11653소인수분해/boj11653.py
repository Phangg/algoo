import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

for i in range(2, N+1):
    while N % i == 0:
        N //= i
        print(i)
    if N == 1:
        break

# def sosu(n):
#     if n == 1:
#         return False
#     for t in range(2, int(n**0.5)+1):
#         if n % t == 0:
#             return False
#     return True
#
# N = int(sys.stdin.readline())
#
# lst = []
# M = N
# while 1:
#     if N == 1:
#         exit()
#     elif N == 2 or N == 3:
#         lst.append(N)
#         break
#     for i in range(2, N+1):
#         if M % i == 0:
#             lst.append(i)
#             M //= i
#             break
#     if sosu(M):
#         lst.append(M)
#         break
# lst.sort()
# for ans in lst:
#     print(ans)