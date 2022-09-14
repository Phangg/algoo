import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(N)]
# print(lst)

stack = []
ans = []
flag = 1
num = 1
for i in range(N):              # lst 를 돌면서 체크
    while num <= lst[i]:        # lst[i] 보다 작거나 같은 동안
        stack.append(num)       # stack 에 추가
        ans.append('+')
        num += 1
    if stack[-1] == lst[i]:     # 그러다가 stack 맨위 숫자랑 같으면
        stack.pop()             # pop
        ans.append('-')
    else:                       # stack 의 맨위가 숫자랑 다르다? 불가능임
        flag = 0                # flag 설정
        print('NO')
        break
if flag:
    for a in ans:
        print(a)