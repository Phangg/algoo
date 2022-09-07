import sys
sys.stdin = open('2Input.txt')

N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

for m in m_lst:
    if m in n_lst:
        print('yes', end=' ')
    else:
        print('no', end=' ')
