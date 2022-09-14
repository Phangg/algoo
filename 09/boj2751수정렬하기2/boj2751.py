import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
for ans in sorted(lst):
    print(ans)