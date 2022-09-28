import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(s):
    q = deque()
    q.append(s)
    visited = [0] * 100001
    while q:
        s = q.popleft()
        for next in [s-1, s+1, s*2]:
            if 0 <= next <= 100000 and not visited[next]:
                if next == K:
                    return visited[s] + 1
                else:
                    q.append(next)
                    visited[next] = visited[s] + 1

N, K = map(int, sys.stdin.readline().split())
ans = 0
if N > K:
    while N != K:
        N -= 1
        ans += 1
elif N < K:
    ans = bfs(N)
print(ans)

'''
100 0 # 100
6 16 # 3
8 20 # 3
15964 89498 # 4781
3 43 # 6
4 27 # 5
5 35 # 5
6 43 # 5
7 43 # 6
100 1 # 99
10 19 # 2
5 19 # 3
1 20 # 5
100000 100000 # 0
0 100000 # 22
100000 0 # 100000
0 1 # 1
3482 45592 # 637
2 4 # 1
9 5 # 4
5 5 # 0
5 17 # 4
'''