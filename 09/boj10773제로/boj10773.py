import sys
sys.stdin = open('input.txt')

K = int(sys.stdin.readline())
stack = []
for _ in range(K):
    num = int(sys.stdin.readline())
    if num:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))
