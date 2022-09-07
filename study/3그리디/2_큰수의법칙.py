import sys
sys.stdin = open('2input.txt')

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

first_n = nums[-1]
second_n = nums[-2]

res = 0
m = 0
while 1:
    for i in range(K):
        res += first_n
        m += 1
        if m == M:
            break
    res += second_n
    m += 1
    if m == M:
        break
print(res)


# N, M, K = map(int, input().split())
# nums = list(map(int, input().split()))
# nums.sort()
#
# first_n = nums[-1]
# second_n = nums[-2]
#
# m, d = divmod(M, (K+1))
# cnt = (m*K) + d
#
# res = 0
# res += (cnt * first_n)
# res += ((M-cnt) * second_n)
#
# print(res)