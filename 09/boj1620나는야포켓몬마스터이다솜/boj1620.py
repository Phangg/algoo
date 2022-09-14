import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
n_dict = dict()
n_lst = []
for i in range(N):
    x = str(sys.stdin.readline().rstrip())
    n_dict[x] = i
    n_lst.append(x)
m_lst = [sys.stdin.readline().rstrip() for _ in range(M)]

for m in m_lst:
    if m.isnumeric():
        print(n_lst[int(m)-1])
    else:
        print(n_dict[m]+1)