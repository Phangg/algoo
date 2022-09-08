import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
a = '"재귀함수가 뭔가요?"'
b1 = '\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
b2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
b3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"'
b4 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
b5 = '라고 답변하였지.'

for i in range(n):
    if i > 0:
        a = ('____') + a
        b1 = ('____') + b1
        b2 = ('____') + b2
        b3 = ('____') + b3
    print(a)
    print(b1)
    print(b2)
    print(b3)
print(('____') + a)
print(('____'*n) + b4)

x = n
for j in range(n+1):
    print(('____'*x) + b5)
    x -= 1