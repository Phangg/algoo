import sys
sys.stdin = open('input.txt')

for _ in range(10):
    X = int(sys.stdin.readline())

    i = 1
    while X > i:
        X -= i
        i += 1

    a = 0
    b = 0

    if i % 2:
        b = X
        a = i-X+1

    else:
        a = X
        b = i-X+1

    print(f'{a}/{b}')