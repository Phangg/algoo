import sys
sys.stdin = open('input.txt')

y_lst = ['*', '+']

T = 10
for tc in range(1, T+1):
    N = int(input())
    SS = input()

# * 다음 + / + 다음 + -> 멈추고 pop , 비우고 push

    # infix -> postfix
    stack = []
    post_lst = []
    for s in SS:
        if s.isdecimal():
            post_lst.append(s)                         # 숫자이면 post에 추가
        else:
            if s == '(':                                    # 여는 괄호 -> 스택 push
                stack.append(s)
            elif s == ')':                                  # 닫는 괄호 ->
                x = stack.pop()
                while x != '(':                             # 여는 괄호 만날 떄 까지 pop해서 post에 추가
                    post_lst.append(x)
                    x = stack.pop()
            elif s == '+':                                  # + 연산자 일 때
                if stack[-1] != '(':                        # 앞에 다른 연산자가 있을 때
                    while stack[-1] != '(':                 # 여는 괄호 만날 떄 까지 pop해서 post에 추가
                        y = stack.pop()
                        post_lst.append(y)
                    stack.append(s)                         # 이후에 + 를 스택에 넣기
                else:
                    stack.append(s)                         # 스택이 비어있거나, 앞에 여는괄호만 있을 때
            else:
                stack.append(s)                             # * 연산자 일 때
    # print(post_lst)

    # postfix 계산
    ans_stack = []
    for p in post_lst:
        if p.isdecimal():
            ans_stack.append(int(p))
        elif p == '*':
            a = ans_stack.pop(-2)
            b = ans_stack.pop(-1)
            ans_stack.append(a*b)
        elif p == '+':
            a = ans_stack.pop(-2)
            b = ans_stack.pop(-1)
            ans_stack.append(a+b)

    print(f'#{tc}', ans_stack[0])