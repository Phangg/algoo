import sys
sys.stdin = open('input.txt')

# 연산자 리스트
y_lst = ['*', '/', '+', '-']

T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())

    #  리스트 내부에서 숫자들을 int로 변환 / 새로운 리스트로 저장
    n_lst = []
    for i in lst:
        if i.isdecimal():
            n_lst.append(int(i))
        else:
            n_lst.append(i)

    # 연산자가 나오면 해당 연산을 진행
    stack = []
    for n in n_lst:
        if n not in y_lst:
            stack.append(n)                         # 연산자가 아닐 때 스택에 넣기
            if n == '.':
                if len(stack) > 2:                  # 잘못된 후위표기식 (숫자가 연산자보다 많을 때)
                    print(f'#{tc}', 'error')
                else:
                    print(f'#{tc}', stack[0])           # 올바른 후위표기식 이면, 스택의 첫 값(최종 연산 값) 출력
        elif n in y_lst and len(stack) > 1:         # 스택에 2개 이상의 숫자가 없다면 잘못된 후위표기식
            a = stack.pop(-2)
            b = stack.pop(-1)
            if n == '*':
                stack.append(a*b)
            elif n == '/':
                stack.append(a//b)                  # 정수로 나타내기 위해 // 사용 -> 문제에서 모두 딱 나누어 떨어진다고 주어짐
            elif n == '+':
                stack.append(a+b)
            elif n == '-':
                stack.append(a-b)
        else:                                       # 잘못된 후위표기식 (숫자보다 연산자가 많을 때)
            print(f'#{tc}', 'error')
            break