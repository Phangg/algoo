from collections import deque

# 현재 좌표에서 다음에 갈 수 있는 좌표를 담은 리스트를 반환 할 함수
def next_coordinate(coordinate, new_b):
    next_c_lst = []
    coordinate = list(coordinate)                                   # 현재 {(), ()} 니까, 리스트로 변환하기
    x1, y1, x2, y2 = coordinate[0][0], coordinate[0][1], coordinate[1][0], coordinate[1][1]
    for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        nx1, ny1, nx2, ny2 = x1+dx, y1+dy, x2+dx, y2+dy
        if (new_b[nx1][ny1] == 0) and (new_b[nx2][ny2] == 0):
            next_c_lst.append({(nx1, ny1), (nx2, ny2)})

    # 로봇 가로로 있을 때
    if x1 == x2:
        if (new_b[x1 - 1][y1] == 0) and (new_b[x2 - 1][y2] == 0):   # 위로 돌릴 수 있어?
            next_c_lst.append({(x1, y1), (x1-1, y1)})
            next_c_lst.append({(x2, y2), (x2-1, y2)})
        if (new_b[x1 + 1][y1] == 0) and (new_b[x2 + 1][y2] == 0):   # 아래로 돌릴 수 있어?
            next_c_lst.append({(x1, y1), (x1+1, y1)})
            next_c_lst.append({(x2, y2), (x2+1, y2)})
    # 로봇 세로로 있을 때
    elif y1 == y2:
        if (new_b[x1][y1 - 1] == 0) and (new_b[x2][y2 - 1] == 0):   # 왼쪽으로 돌릴 수 있어?
            next_c_lst.append({(x1, y1), (x1, y1 - 1)})
            next_c_lst.append({(x2, y2), (x2, y2 - 1)})
        if (new_b[x1][y1 + 1] == 0) and (new_b[x2][y2 + 1] == 0):   # 오른쪽으로 돌릴 수 있어?
            next_c_lst.append({(x1, y1), (x1, y1 + 1)})
            next_c_lst.append({(x2, y2), (x2, y2 + 1)})

    return next_c_lst


# 길이가 2인 로봇이 지나다니면서 체크할 것..
# 더미를 만들어서 하면, 범위를 거를 일이 줄어든다..
def solution(board):
    n = len(board)
    new_b = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_b[i+1][j+1] = board[i][j]
    # print(new_b)
    q = deque()
    visited = []
    start = {(1, 1), (1, 2)}                                # 문제의 값.. 리스트로 하면 시간이 엄청 길어진다.
    q.append((start, 0))                                    # 시간을 가지고 다니면서 최소시간 구하기
    visited.append(start)
    while q:
        coordinate, sec = q.popleft()
        if (n, n) in coordinate:                            # 도착지가 좌표에 들어있다면, 시간 반환 및 종료
            return sec
        for next_c in next_coordinate(coordinate, new_b):   # 현 좌표에서 갈 수 있는 곳을 가진 리스트 만드는 함수 돌고 오기
            if next_c not in visited:                       # 방문 한적 없으면, q 랑 visited 에 추가
                q.append((next_c, sec + 1))
                visited.append(next_c)

    return 0


board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]
print(solution(board))