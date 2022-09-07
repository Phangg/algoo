import sys
sys.stdin = open('input.txt')

# 10라운드
# 이기면 3점 지면 0점 비기면 1점
# 총점 비교 / A or B (총점은 같으면 제일 최근 이긴 사람 승) or D (10판 전부 비기면)

a_score = list(map(int, sys.stdin.readline().split()))
b_score = list(map(int, sys.stdin.readline().split()))

A, B, D = 0, 0, 0
lst = []
for score in range(10):
    if a_score[score] > b_score[score]:
        A += 3
        lst.append('A')
    elif a_score[score] < b_score[score]:
        B += 3
        lst.append('B')
    else:
        A += 1
        B += 1
        D += 1

if A > B:
    print(A, B)
    print('A')
elif A < B:
    print(A, B)
    print('B')
elif D == 10:
    print(A, B)
    print('D')
else:
    print(A, B)
    print(lst[-1])