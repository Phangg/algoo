import sys
sys.stdin = open('input.txt')

s = sys.stdin.readline().rstrip()
n = len(s)
res = set()
i = 1
while i <= n:
    for k in range(n-i+1):
        res.add(s[k:k+i])
    i += 1
print(len(res))