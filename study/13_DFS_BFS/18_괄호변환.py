# p 를 u 와 v 로 나누기
def make_uv(p):
    open_p = 0
    close_p = 0
# 여는 괄호 , 닫는 괄호 숫자 체크 -> 같은 경우라면,
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i+1], p[i+1:]

# u 가 '올바른 괄호 문자열' 인지 체크
def u_is_real(u):
    stack = []
    for j in u:
        if j == '(':            # 여는 괄호일때, stack
            stack.append(j)
        else:                   # 닫는 괄호일때,
            if not stack:       # 스택 비어있으면, False 반환
                return False
            stack.pop()         # pop
    return True

# 첫 시작
def solution(p):
    # p가 빈 문자열이라면 그대로 반환
    if not p:
        return ""

    # u, v 나누기
    u, v = make_uv(p)

    answer = ''
    # u 가 '올바른 괄호 문자열' 일때, 문자열 v에 대해 1단계부터 다시 수행합니다.
    if u_is_real(u):
        return u + solution(v)
    # u 가 '균형잡힌 괄호 문자열' 일때,
    else:
        # 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        answer += '('
        # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        answer += solution(v)
        # ')'를 다시 붙입니다.
        answer += ')'
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        for k in u[1:len(u)-1]:
            if k == '(':
                answer += ')'
            else:
                answer += '('

    # 생성된 문자열을 반환합니다.
    return answer


# p = "(()())()"
# p = ")("
p = "()))((()"
print(solution(p))