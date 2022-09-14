import sys
sys.stdin = open('input.txt')

x, y, w, h = map(int, sys.stdin.readline().split())
# print(x, y, w, h)

print(min(h-y, w-x, x-0, y-0))