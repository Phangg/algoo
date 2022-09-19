import sys
sys.stdin = open('input.txt')

L = int(sys.stdin.readline())
x = list(sys.stdin.readline().rstrip())

res = 0
for idx, v in enumerate(x):
    res += (ord(v)-96) * (31**idx)
print(res % 1234567891)
