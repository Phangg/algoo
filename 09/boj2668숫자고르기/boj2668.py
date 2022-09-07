import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
visited = [False] * (N+1)
n_lst = list(range(1, N+1))
m_lst = [int(sys.stdin.readline()) for _ in range(N)]
# print(n_lst)
# print(m_lst)
arr = [[] for _ in range(N+1)]
for i in range(N):
    arr[m_lst[i]].append(n_lst[i])
print(arr)

