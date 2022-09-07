import sys
sys.stdin = open('input.txt')

def my_max(x):
    max_n = 0
    for i in x:
        if i > max_n:
            max_n = i
    return max_n

def my_min(x):
    min_n = 101
    for i in x:
        if i < min_n:
            min_n = i
    return min_n

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    lst = [0] * 10
    for n in range(10):
        if n % 2:
            lst[n] = my_min(nums)
            nums.pop(nums.index(my_min(nums)))
        else:
            lst[n] = my_max(nums)
            nums.pop(nums.index(my_max(nums)))

    print(f'#{tc}', *lst)