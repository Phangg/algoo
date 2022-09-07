import sys
sys.stdin = open('3input.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    min_lst = []
    for row in lst:
        min_lst.append(min(row))

    print(max(min_lst))