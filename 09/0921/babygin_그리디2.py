import sys
sys.stdin = open('input_babygin.txt')

T = int(input())
for _ in range(T):
    card = int(input())
    c = [0] * 12

    i = 0
    while i < 6:
        c[card % 10] += 1
        card //= 10
        i += 1
    # print(c)

    tri = run = 0
    i = 1
    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1
            continue
        i += 1
    if run + tri == 2:
        print('BabyGin')
    else:
        print('Lose')