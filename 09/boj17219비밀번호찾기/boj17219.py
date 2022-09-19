import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
dic = dict()
for _ in range(N):
    domain, pw = sys.stdin.readline().split()
    dic[domain] = pw
for _ in range(M):
    print(dic[sys.stdin.readline().rstrip()])