import sys
sys.stdin = open('input.txt')

def max_n(lst):
    max_b = -1
    max_idx = -1
    for i in range(len(lst)):
        if lst[i] > max_b:
            max_b = lst[i]
            max_idx = i
    return max_idx

def min_n(lst):
    min_b = 101
    min_idx = 101
    for i in range(len(lst)):
        if lst[i] < min_b:
            min_b = lst[i]
            min_idx = i
    return min_idx

T = 10
for tc in range(1, T + 1):
    D = int(input())
    box_h = list(map(int, input().split()))

    for d in range(D):
        box_h[max_n(box_h)] -= 1
        box_h[min_n(box_h)] += 1
    result = box_h[max_n(box_h)] - box_h[min_n(box_h)]

    print(f'#{tc} {result}')


