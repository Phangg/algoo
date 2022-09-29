import sys
sys.stdin = open('input.txt')

A, B = map(int, sys.stdin.readline().split())
a_set = set(map(int, sys.stdin.readline().split()))
b_set = set(map(int, sys.stdin.readline().split()))
x = a_set - b_set
y = b_set - a_set
print(len(x) + len(y))