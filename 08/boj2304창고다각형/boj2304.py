import sys
sys.stdin = open('input.txt')

lst = [0] * 1001                                        # N이 1 이상 1000이하
max_h = 0                                               # 제일 높은 위치 값
max_h_idx = 0                                           # 제일 높은 위치 인덱스
max_w_idx = 0                                           # 제일 끝 기둥 인덱스

N = int(sys.stdin.readline())
for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    lst[L] = H
    if max_h < H:                                       # H 입력마다 비교해서 제일 높은 위치 값, 인덱스 구하기
        max_h = H
        max_h_idx = L
    max_w_idx = max(max_w_idx, L)                       # L 입력마다 비교해서, 값 구하기


stack = []                                              # 빈 스택
ans = 0                                                 # 결과 값 -> 누적될 창고 다각형 면적
for i in range(max_h_idx+1):                            # 제일 높은 곳 까지
    if not stack:                                       # 스택 비어있다면
        stack.append(lst[i])
        ans += stack[-1]                                # 스택에 추가 / 스택 마지막 값 ans 에 더하기
    else:
        if stack[-1] < lst[i]:                          # 스택의 마지막 값보다 높은 값을 가진다면
            stack.pop()                                 # 마지막 값 pop
            stack.append(lst[i])                        # 더 높은 값 스택에 추가
        ans += stack[-1]                                # 위 if 문을 통과하지 못하더라도 스택 맨 위 값 ans 에 더하기

stack = []
for i in range(max_w_idx, max_h_idx, -1):               # 위 로직을 뒤에서부터 제일 높은 곳 직전까지 같은 방법으로 진행
    if not stack:
        stack.append(lst[i])
        ans += stack[-1]
    else:
        if stack[-1] < lst[i]:
            stack.pop()
            stack.append(lst[i])
        ans += stack[-1]

print(ans)