import sys
sys.stdin = open('input.txt')

N, M, L = map(int, sys.stdin.readline().split())
lst = [0] * (N+1)
x = 1
ans = 0
while lst[x] != M-1:
    lst[x] += 1
    if lst[x] % 2:
        x += (L % N)
        if x > N:
            x -= N
    else:
        x -= (L % N)
        if x <= 0:
            x += N
    ans += 1
print(ans)