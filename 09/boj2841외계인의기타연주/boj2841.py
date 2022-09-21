import sys
sys.stdin = open('input.txt')

N, P = map(int, sys.stdin.readline().split())
cnt = 0
x = 0
stack = [[] for _ in range(N+1)]
# print(stack)
for _ in range(N):
    line, pr = map(int, sys.stdin.readline().split())
    if x != line and len(stack[line]) == 0:
        x = line
        stack[line].append(pr)
        cnt += 1
    else:
        if stack[line]:
            if stack[line][-1] > pr:
                while stack[line][-1] > pr:
                    stack[line].pop()
                    cnt += 1
                    if len(stack[line]) == 0:
                        break
                if len(stack[line]) == 0:
                    stack[line].append(pr)
                    cnt += 1
                elif stack[line][-1] != pr:
                    stack[line].append(pr)
                    cnt += 1
            elif stack[line][-1] < pr:
                stack[line].append(pr)
                cnt += 1
        else:
            stack[line].append(pr)
            cnt += 1
print(cnt)
# print(stack)


