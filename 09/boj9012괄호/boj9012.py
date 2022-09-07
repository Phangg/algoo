import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    lst = list(sys.stdin.readline().rstrip())
    # print(lst)

    stack = []
    for v in lst:
        if len(stack) == 0 :
            if v == ')':
                stack.append(v)
            else:
                stack.append(v)
        else:
            if v == ')':
                if stack[-1] == '(':
                    stack.pop(-1)
            else:
                stack.append(v)
    # print(stack)
    if stack:
        print('NO')
    else:
        print('YES')