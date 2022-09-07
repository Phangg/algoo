
## 딕셔너리 이용

exp = "(6+5*(2-8)/2)"
stack = [] # 우리가 후위 표기법으로 변환시키기 위해 필요한 중간 저장소
res = [] # 후위 표기법이 저장될 장소

isp = {
    '*':2,
    '/':2,
    '-':1,
    '+':1,
    '(':0,
}
icp = {
    '*':2,
    '/':2,
    '-':1,
    '+':1,
    '(':3,
}


for token in exp:
    # 2
    if token.isdecimal():
        res.append(int(token))
    else:
        if stack:
            # 차있는경우
            # 3.2
            if token == ")":
                tmp = stack.pop()
                while tmp != "(":
                    res.append(tmp)
                    tmp = stack.pop()
            elif icp[token] > isp[stack[-1]]:
                stack.append(token)
            # 3.3
            else:
                while stack and icp[token] <= isp[stack[-1]]:
                    res.append(stack.pop())
                stack.append(token)
        # 3.1
        else:
            #비어있는 경우
            stack.append(token)

res.extend(stack[::-1])

# 하나하나 비교하면서 


infix = "(6+5*(2-8)/2)"
stack = []
result = []
for token in infix:

    if token.isdigit():
        result.append(token)

    else:
        if not stack:
            stack.append(token)

        else:
            if token == "(":
                stack.append(token)
            elif token == ")":
                tmp = stack.pop()
                while tmp != "(":
                    result.append(tmp)
                    tmp = stack.pop()
            elif token == "*" or token == "/":
                while stack and stack[-1] == "*" or stack[-1] == "/":
                    result.append(stack.pop())
                stack.append(token)

            elif token == "+" or token == "-":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.append(token)

for _ in range(len(stack)):
    result.append(stack.pop())

print(result)


# 후위 표기식 계산

for token in result:
    if token.isdecimal():
        # result에 들어있는 숫자가 int 형이 아닌 경우
        stack.append(int(token))
        # result에 들어있는 숫자가 int 형인 경우
        # stack.append(token)
    else:
        if token == "+":
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(p2+p1)
        elif token == "-":
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(p2-p1)
        elif token == "*":
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(p2*p1)
        elif token == "/":
            p1 = stack.pop()
            p2 = stack.pop()
            stack.append(p2/p1)
ans = stack.pop()










