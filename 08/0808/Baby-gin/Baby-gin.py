import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    arr = list(map(int, input()))

    c_lst = [0] * 10
    for i in range(len(arr)):
        c_lst[arr[i]] += 1

    i = 0
    run = 0
    tri = 0
    while i < 10:
        if c_lst[i] >= 3:
            tri += 1
            c_lst[i] -= 3
            continue
        if c_lst[i] >= 1 and c_lst[i+1] >= 1 and c_lst[i+2] >= 1:
            run += 1
            c_lst[i] -= 1
            c_lst[i+1] -= 1
            c_lst[i+2] -= 1
            continue
        i += 1

    if run + tri == 2:
        print('baby gin')
    else:
        print('nope')
