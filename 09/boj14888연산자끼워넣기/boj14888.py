# python3 통과

import sys
sys.stdin = open('input.txt')

# cnt: 계산 횟수 / total: 계산 된 숫자 / p: '+' / m: '-' / x: '*' / y: '/'
def solve(cnt, total, p, m, x, y):
    global max_v, min_v
    if cnt == N:
        max_v = max(max_v, total)
        min_v = min(min_v, total)
        return

    if p:
        solve(cnt+1, total + A[cnt], p-1, m, x, y)
    if m:
        solve(cnt+1, total - A[cnt], p, m-1, x, y)
    if x:
        solve(cnt+1, total * A[cnt], p, m, x-1, y)
    if y:
        solve(cnt+1, int(total / A[cnt]), p, m, x, y-1)



N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
op_num = list(map(int, input().split()))
# ['+', '-', '*', '/']

max_v = -1000000001
min_v = 1000000001

solve(1, A[0], op_num[0], op_num[1], op_num[2], op_num[3])

print(max_v)
print(min_v)