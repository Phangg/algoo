import sys
sys.stdin = open('3input.txt')

N = int(input())
lst = []
for _ in range(N):
    name, score = input().split()
    lst.append([name, int(score)])
lst.sort(key=lambda x: x[1])
for i in lst:
    print(i[0], end=' ')