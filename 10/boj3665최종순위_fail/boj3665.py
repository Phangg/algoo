import sys
from collections import deque
sys.stdin = open('input.txt')

# def topology():
#     q = deque()
#     res = []

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    last_lst = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    change = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    indegree = [0] * (n+1)
    n_graph = [[] for _ in range(n+1)]
    for i in range(n-1):
        for j in range(i+1, n):
            n_graph[last_lst[i]].append(last_lst[j])
            indegree[last_lst[j]] += 1
    # print(indegree)
    # print(n_graph)
