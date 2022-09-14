import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

lst.sort(key=lambda x: (x[1], x[0]))
# print(lst)

for ans in lst:
    print(*ans)