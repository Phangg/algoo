import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    n = list(input())

# infix -> postfix
# + 다음 + 가 올 때
# * 다음 + 가 올 때
# 멈추고 pop / 스택 비우고 들어가려던 + push

    lst = ['+', '*']                                    # 존재하는 연산자
    stack1 = []                                         # 연산자 보관 스택
    postfix_s = ''                                      # 만들어낼 후위 표기식 문자열
    for i in range(N):
        if n[i] not in lst:                             # 연산자가 아닐 경우
            postfix_s += n[i]                           # 문자열에 추가
        elif n[i] == '+' and len(stack1) != 0:          # 연산자가 + 이고 스택이 비어있지 않을 때
            x = ''
            while len(stack1) > 0:                      # 스택이 빌때까지
                x = stack1.pop()                        # pop 해서
                postfix_s += x                          # 문자열에 추가
            stack1.append(n[i])                         # while 끝나면 스택에 + 추가
        else:
            stack1.append(n[i])                         # 스택에 추가
    while len(stack1) > 0:
        postfix_s += stack1.pop()                       # 마지막 남은 연산자 다 뽑아서 문자열에 추가
    # print(postfix_s)
    # print(len(postfix_s))

# postfix 계산
    stack2 = []
    for j in range(N):                                  # 후위 표기식을 순회
        if postfix_s[j] not in lst:                     # 연산자가 아니라면
            stack2.append(postfix_s[j])                 # 스택에 넣어주기
        elif postfix_s[j] in lst:                       # 연산자일 때,
            a = int(stack2.pop(-2))                     # 스택 위에서 두번째 (숫자) int 변환
            b = int(stack2.pop())                       # 스택 맨위 (숫자) int 변환
            if postfix_s[j] == '*':
                stack2.append(a*b)
            else:                                       # 연산자가 뭐였는지에 따라, 계산하여 스택에 다시 삽입
                stack2.append(a+b)
    print(f'#{tc}', stack2[-1])                         # 스택에 마지막에 있을 하나의 숫자가 최종 연산 결과