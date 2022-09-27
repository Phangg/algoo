import sys
from collections import deque

sys.stdin = open('input.txt')

n = int(sys.stdin.readline().rstrip())
lst = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))
fish = [0] * 7
shark = 2
time = 0
grow = 0

for i in range(n):
    for j in range(n):
        if lst[i][j] == 9:
            x_s, y_s = i, j
            lst[i][j] = 0
        elif lst[i][j]:
            fish[lst[i][j]] += 1

# print(fish)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

q = deque()
q.append((x_s, y_s, time))

def bfs():
    global time, shark, grow, q, visited, fish
    visited = []
    food = []
    eat = None
    record = q[0][2]
    while q:
        x, y, time = q.popleft()
        if 0 < lst[x][y] < shark:
            if not eat:
                eat = time
                food.append((x, y, time))
            elif eat == time:
                food.append((x, y, time))
            else:
                eat = None
                break
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < n and lst[x + dx[i]][y + dy[i]] <= shark and (x + dx[i], y + dy[i]) not in visited:
                q.append((x + dx[i], y + dy[i], time + 1))
                visited.append((x + dx[i], y + dy[i]))
    if food:
        food.sort()
        x, y, time = food[0]
        q = deque()
        q.append((x, y, time))
        fish[lst[x][y]] -= 1
        lst[x][y] = 0
        grow += 1
        if grow == shark:
            grow = 0
            shark += 1
    else:
        time = record
        fish = [0] * 7

while sum(fish[:shark]):
    bfs()

print(time)