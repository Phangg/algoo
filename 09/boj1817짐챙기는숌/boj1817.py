import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
if N == 0:
    print(0)
    exit()
else:
    books = list(map(int, sys.stdin.readline().split()))[::-1]

box = 1
weight = 0
while books:
    x = books.pop()
    if x + weight <= M:
        weight += x
    else:
        box += 1
        weight = x
print(box)