import sys
sys.stdin = open('2input.txt')

N = int(input())
num = list(int(input()) for _ in range(N))
num.sort(reverse=True)
print(*num)