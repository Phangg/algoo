import sys
sys.stdin = open('input.txt')

A = int(sys.stdin.readline())
a_lst = list(map(int, sys.stdin.readline().split()))

for i in range(A):
    max_a = 0
    for j in range(i+1, A):
        if a_lst[i] < a_lst[j]:
            max_a = a_lst[j]
            break
    if max_a:
        print(max_a, end=' ')
    else:
        print(-1, end=' ')
print()