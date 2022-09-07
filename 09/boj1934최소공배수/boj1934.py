import sys
sys.stdin = open('input.txt')

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a * b // gcd(a, b))