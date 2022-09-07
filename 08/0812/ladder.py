import sys
sys.stdin = open('input.txt')
dx = [0, 0, -1]
dy = [1, -1, 0]
# set을 사용한 방문처리
for _ in range(10):
    case = int(input())
    n = 100
    lst = [list(map(int,input().split())) for _ in range(100)]
    y = lst[-1].index(2)
    x = 100 - 1 # 99
    visited = set()

    while x>0:
        visited.add((x,y))
        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nx<n and 0<=ny<n and lst[nx][ny]==1 and (nx,ny) not in visited:
                x = nx
                y = ny

    print(y)


# for _ in range(10):
#     case = int(input())
#     n = 100
#     lst = [list(map(int,input().split())) for _ in range(100)]
#     y = lst[-1].index(2)
#     x = 100 - 1 # 99
#     visited = [[0]*n for _ in range(n)]
#     while x>0:
#         visited[x][y] == 1
#         for d in range(3):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if 0<=nx<n and 0<=ny<n and lst[nx][ny]==1 and visited[nx][ny] == 0:
#                 x = nx
#                 y = ny
#
#     print(y)
















# for _ in range(10):
#     case = int(input())
#     n = 100
#     lst = [list(map(int,input().split())) for _ in range(100)]
#     y = lst[-1].index(2)
#     x = 100 - 1 # 99
#     while x>0:
#         for d in range(3):
#             nx = x + dx[d]
#             ny = y + dy[d]
#             if 0<=nx<n and 0<=ny<n and lst[nx][ny]==1:
#                 lst[x][y] = 0
#                 x = nx
#                 y = ny
#
#     print(y)









