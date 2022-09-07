import sys
sys.stdin = open('input.txt')

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# class Stack:
#
#     def __init__(self, size):
#         self.size = size
#         self.data = [0] * size
#         self.top = -1
#
#     def push(self, x):
#         self.data[self.top + 1] = x
#         self.top += 1
#
#     def pop(self):
#         x = self.data[self.top]
#         self.top -= 1
#         return x
#
#     def size(self):
#         return self.top + 1
#
#     def empty(self):
#         if self.top == -1:
#             return 1
#         else:
#             return 0
#
#     def top(self):
#         if self.top == -1:
#             return -1
#         else:
#             return self.data[self.top]

N = int(input())
stack = []                                      # stack 과 top 설정
top = -1

for _ in range(N):
    action = input().split()
    act = action[0]

    if act == 'push':
        stack.append(action[1])
        top += 1
    elif act == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack.pop())
            top -= 1
    elif act == 'size':
        print(top + 1)
    elif act == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif act == 'top':
        if top == -1:
            print(-1)
        else:
            print(stack[top])