import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input.txt')

def bfs(arr, x, y):
    q = deque()                                                         # deque 선언
    q.append((x, y))                                                    # 시작점 추가
    arr[x][y] = 0                                                       # 시작점 0으로 바꾸기
    cnt = 1                                                             # 시작점 / cnt 1부터 시작

    while q:
        x, y = q.popleft()                                              # q 가 차있는 동안 진행 / x,y를 q 에서 뽑은 값으로 재 설정
        for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:                   # 델타 탐색
            nx, ny = x+dx, y+dy
            if (0 <= nx < N) and (0 <= ny < N) and (arr[nx][ny] == 1):  # 범위 안쪽 + 갈 곳이 1이어야 함
                q.append((nx, ny))                                      # q에 현재 인덱스 추가 (이동 시, 위치 저장)
                arr[nx][ny] = 0                                         # 도착한 곳 0으로 바꾸기
                cnt += 1                                                # cnt
    return cnt

# lst 받을 때 인풋 공백없음 / sys 로 받으면 맨뒤에 \n 개행이 자동으로 붇기에 rstrip() 사용
N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
# pprint(lst)

ans = []
for i in range(N):                              # 2차원 배열 lst를 돌면서 1이 나오면 bfs 함수를 실행 -> 반환 값 ans에 넣기
    for j in range(N):
        if lst[i][j] == 1:
            ans.append(bfs(lst, i, j))
# print(ans)

ans.sort()
print(len(ans))
for a in ans:
    print(a)
