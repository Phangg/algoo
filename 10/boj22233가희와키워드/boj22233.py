import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
keywords = set(sys.stdin.readline().rstrip() for _ in range(N))
for _ in range(M):
    keywords -= set(sys.stdin.readline().rstrip().split(','))
    print(len(keywords))
