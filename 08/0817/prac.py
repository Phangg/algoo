# 스택

stackSize = 10
stack = [0] * stackSize
top = -1

top += 1                # top 증가
stack[top] = 1          # push(1)

top += 1
stack[top] = 2          # push(2)

top -= 1
temp = stack[top + 1]   # pop
print(temp)

temp = stack[top]
top -= 1                # pop
print(temp)

print()
#-------------------------------------------------------------
stack2 = []
stack2.append(10)
stack2.append(20)
print(stack2.pop())
print(stack2.pop())

print()
#-------------------------------------------------------------

# 재귀

def f(i, N):                # i 는 현재 단계 / N 은 목표 단계
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)

f(0, 3)

print()
#-------------------------------------------------------------

# 크기가 N 인 배열의 모든 원소에 접근하는 재귀 함수

def f(i, N):
    if i == N:              # 배열을 벗어남
        return
    else:                   # 남은 원소가 있는 경우
        B[i] = A[i]
        f(i+1, N)           # 다음 원소로 이동

N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N)                     # 0번 원소부터 N개의 원소에 접근
print(B)

print()
#-------------------------------------------------------------

class Stack:

    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.top = -1

    def push(self, value):
        if self.is_full():          # is_full 함수로 가서 확인
            print('overflow')
        else:
            self.top += 1
            self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            print('underflow')
        else:
            value = self.data[self.top]
            self.data[self.top] = None
            self.top -= 1
            return value

    def peek(self):
        if self.is_empty():
            print('underflow')
        else:
            return self.data[self.top]

    def is_full(self):              # 만약 가득 찼다면~
        return self.top + 1 == self.size
        # if self.size == self.top + 1:
        #     return True
        # else:
        #     return False

        # return True if self.size == self.top + 1 else False

    def is_empty(self):
        return self.top == -1

    def length(self):
        return self.top + 1

    def __str__(self):
        return f'{self.data}'

stack = Stack(3)                    # size 3 의 Stack 클래스 속성을 가지는 stack 설정
stack.push(1)
print(stack)

stack.push(2)
stack.pop()
print(stack)

stack.push(2)
print(stack)

stack.push(3)
print(stack)

stack.pop()
print(stack)

stack.push(3)
stack.push(4)                       # 가득 차있기 때문에, 에러 발생 -> if 문을 만들어서 overflow 표시
print(stack)


print()
#-------------------------------------------------------------

# 팩토리얼

def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

for i in range(11):
    print(i, f(i))

print()
#-------------------------------------------------------------

# 피보나치

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(21):
    print(i, fibo(i))

print()
#-------------------------------------------------------------

# 숫자가 커질 때, 위에 있는 코드보다 시간이 적게 소요 - memoization
def fibo(n):
    if memo[n] == None:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [None] * 21
memo[0] = 0
memo[1] = 1

for i in range(21):
    print(i, fibo(i))

print()
#-------------------------------------------------------------

# 피보나치 - DP

def fibo_dp(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i-1] + table[i-2]
    return

table = [0] * 101
fibo_dp(100)
print(table[100])

print()
#-------------------------------------------------------------

a = 0
b = 1
n = 100
for _ in range(n-1):
    a, b = b, a+b
print(b)

print()
#-------------------------------------------------------------

# DFS
# A ~ G -> 0 ~ 6
adjlst = [[1, 2],                   # 0
          [0, 3, 4],                # 1
          [0, 4],                   # 2
          [1, 5],                   # 3
          [1, 2, 5],                # 4
          [3, 4, 6],                # 5
          [5]]                      # 6

def dfs(v, N):
    top = -1
    print(v)                        # 정점 도착
    visited[v] = 1                  # 시작점 방문 표시
    while True:
        for w in adjlst[v]:         # if ( v 의 인접 정점 중 방문 안 한 정점 w 가 있으면)
            if visited[w] == 0:     # 방문하지 않은 w
                top += 1            # push(v)
                stack[top] = v
                v = w               # v <- w
                visited[w] = 1      # visited[w] <- true
                print(v)            # 정점 도착
                break
        else:                       # w 가 없으면
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break
N = 7
visited = [0] * N                   # visited 생성
stack = [0] * N                     # stack 생성
dfs(0, N)

