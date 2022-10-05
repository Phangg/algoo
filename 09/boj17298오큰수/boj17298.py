import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
a_lst = list(map(int, sys.stdin.readline().split()))

ans = [-1] * N
stack = []
for idx, a in enumerate(a_lst):
    if not stack:
        stack.append((idx, a))
    elif stack[-1][1] >= a:
        stack.append((idx, a))
    else:
        while stack and stack[-1][1] < a:
            i = stack[-1][0]
            ans[i] = a
            stack.pop()
        stack.append((idx, a))
print(*ans)