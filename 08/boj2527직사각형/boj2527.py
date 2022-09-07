import sys
sys.stdin = open('input.txt')

# A, B 두 사각형
T = 4
for _ in range(T):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, sys.stdin.readline().split())
    # print(x1, y1, p1, q1, x2, y2, p2, q2)
    if x2 > p1 or x1 > p2 or q2 < y1 or y2 > q1:
        print('d')

    elif x1 == p2 or x2 == p1:
        if q1 == y2 or y1 == q2:
            print('c')
        else:
            print('b')

    elif q1 == y2 or q2 == y1:                      # 바로 위 elif 조건이 먼저 진행 되어야 함.
        print('b')

    else:
        print('a')


