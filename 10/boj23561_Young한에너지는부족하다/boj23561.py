import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
print(lst[2*N-1] - lst[N])
