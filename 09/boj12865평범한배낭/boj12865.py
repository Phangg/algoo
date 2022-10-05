import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

item = []
value = [0] * (K+1)

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    item.append((W, V))

for i in item:
    w, v = i

    for t in range(K, w-1, -1):
        value[t] = max(value[t], value[t-w] + v)

print(value[-1])