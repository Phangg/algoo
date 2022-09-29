import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
n_card = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_card = list(map(int, sys.stdin.readline().split()))

ans = []
for m in m_card:
    if m in n_card:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)