# 유클리드 호제법

# 2개의 자연수 또는 정식의 최대 공약수를 구하는 알고리즘의 하나

# EX) 1071 과 1029 의 최대 공약수
# 1071은 1029로 나누어 떨어지지 않기 때문에, 1071을 1029로 나눈 나머지를 구한다. ≫ 42
# 1029는 42로 나누어 떨어지지 않기 때문에, 1029를 42로 나눈 나머지를 구한다. ≫ 21
# 42는 21로 나누어 떨어진다.
# 따라서, 최대공약수는 21이다.

# # 최대 공약수
# def b_eu(m, n):
#     if m < n:
#         m, n = n, m
#     if n == 0:
#         return m
#     if m % n == 0:
#         return n
#     else:
#         return eu(n, m % n)

# 최대 공약수
def b_eu(m, n):
    while n > 0:
        m, n = n, m%n
    return m

# 최대 공배수
def s_eu(m, n):
    return m * n // b_eu(m, n)

m = 1071
n = 1029
print(b_eu(m, n))
print(s_eu(m, n))

print()

# math
import math

a = 1071
b = 1029
print(math.gcd(a, b))
print(math.lcm(a, b))

