import sys
from copy import deepcopy
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')

def bfs(tmp_lst):
    while tmp_lst:
        i, j = tmp_lst.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            while (0 <= ni < n) and (0 <= nj < n) and (arr[ni][nj] != 'O'):
                if arr[ni][nj] == 'S':
                    return True
                else:
                    ni += di
                    nj += dj
    return False

n = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(n)]

# bfs 돌거라서, 선생님 좌표는 deque 에 append
t_lst = deque()
o_lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'T':
            t_lst.append((i, j))
        elif arr[i][j] == 'X':
            o_lst.append((i, j))

# 장애물 좌표리스트를 가지고 콤비네이션 진행
comb_lst = list(combinations(o_lst, 3))
# print(comb_lst)

# 콤비네이션 리스트를 가지고 좌표 뽑아서 장애물 만들기
# bfs 돌고 아니면 장애물 원위치
# 돌 때, 선생님 리스트가 deque 에서 변화가 생기니, deepcopy 해서 체크하기
for coordinate in comb_lst:
    tmp_lst = deepcopy(t_lst)
    x1, y1 = coordinate[0]
    x2, y2 = coordinate[1]
    x3, y3 = coordinate[2]
    arr[x1][y1] = 'O'
    arr[x2][y2] = 'O'
    arr[x3][y3] = 'O'
    res = bfs(tmp_lst)
    if not res:
        print('YES')
        break
    arr[x1][y1] = 'X'
    arr[x2][y2] = 'X'
    arr[x3][y3] = 'X'
else:
    print('NO')