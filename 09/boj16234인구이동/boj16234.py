import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs_check(x, y):
    q = deque()
    q.append([x, y])
    check[x][y] = 1         # 지나갈 수 있는 곳을 저장
    res = []                # 나중에 바뀐 값 인덱스 저장 리스트
    res.append([x, y])
    cnt = 1                 # 지나간 곳 개수 카운트
    tmp = False             # 인구 이동 ? Yes or No
    total = people[x][y]    # 인구 수 합
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x+dx, y+dy

            # 범위를 벗어나지 않아야 하고, 지나간 적이 없고, 현재와 다음의 인구수 차이가 L 이상 R 이하인 경우
            if (0 <= nx < N) and (0 <= ny < N) and (check[nx][ny] == 0) and (L <= abs(people[x][y]-people[nx][ny]) <= R):
                # 인구 이동 체크
                if not tmp and ((total // cnt) != people[nx][ny]):
                    tmp = True
                check[nx][ny] = 1
                q.append([nx, ny])
                res.append([nx, ny])
                cnt += 1
                total += people[nx][ny]
    if tmp:                                 # 인구 이동 시,
        mid = (total // cnt)
        for a in res:                       # 인구수 평균값으로 변경
            p, q = a[0], a[1]
            people[p][q] = mid
        return True                         # True 반환
    else:
        return False


N, L, R = map(int, sys.stdin.readline().split())
people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(people)

ans = 0                                                 # 답
while 1:
    check = [[0] * N for _ in range(N)]                 # 체크용
    flag = 0                                            # 플래그
    for i in range(N):
        for j in range(N):
            if not check[i][j] and bfs_check(i, j):     # 0인 곳  /  함수 값 True 일 때, 체크
                # print(check)
                # print(people)
                flag = 1
    if flag:
        ans += 1
    else:
        break
# print(check)
# print(people)
print(ans)