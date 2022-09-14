import sys
sys.stdin = open('input.txt')

lst = list(map(int, sys.stdin.readline().split()))

a, d = 0, 0
for i in range(1, 8):
    if lst[i] > lst[i-1]:
        a += 1
    elif lst[i] < lst[i-1]:
        d += 1
if a == 7:
    print('ascending')
elif d == 7:
    print('descending')
else:
    print('mixed')