import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    S = input()

    stack = [None] * len(S)                     # 입력값 크기만큼의 스택
    top = -1
    dic = {')': '(', '}': '{'}                  # 닫는 괄호 key / 여는 괄호 value 딕셔너리 생성
    for i in S:
        if '(' == i or '{' == i:                # 여는 괄호
            stack[top + 1] = i                  # 스택에 넣기
            top += 1
        elif ')' == i or '}' == i:              # 닫는 괄호
            if stack[top] == dic[i]:            # 스택에서 같은 종류 여는 괄호가 맨 위에 있는지 딕셔너리로 확인 / pop
                stack.pop(top)
                top -= 1
            else:
                top += 1                        # 닫는 괄호가 맨 앞에 나오는 경우 -> top 에 고의적으로 +1 / break
                break

    if top == -1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')