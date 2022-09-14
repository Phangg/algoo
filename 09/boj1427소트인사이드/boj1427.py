import sys
sys.stdin = open('input.txt')

n = list(map(int, sys.stdin.readline().rstrip()))
n.sort(reverse=True)
# print(n)
for i in n:
    print(i, end='')