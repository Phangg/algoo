# 지그 재그 순회
n = 3
m = 4
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


for i in range(n):
    for j in range(m):
        print(arr[i][j + (m-1-2*j) * (i%2)], end=' ')
        # 인덱스 3 2 1 0 순으로 오려면 m-1-j 면 된다.
        # 이때 여기서 행마다 변화하므로,
        # i 가 짝수 행일 때 정상 작동 하기 위해,
        # j 하나는 밖으로 두고 (m-1-2*j) 를 넣어 줌
print()

for i in range(n):
    for j in range(m):
        if i % 2:
            print(arr[i][-1-j], end=' ')
        else:
            print(arr[i][j], end=' ')
print()

# -------------------------------------------------------

# 델타 이용 2차원 배열
# i 행 , j 열
# 오른쪽 부터 시계 방향으로 체크
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = 3
M = 4
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for i in range(N):
    for j in range(M):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)

# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# for i in range(N):
#     for j in range(M):
#         for d in range(1, 3):
#             for k in range(4):
#                 ni = i + di[k] * d
#                 nj = j + dj[k] * d
#                 if 0 <= ni < N and 0 <= nj < M:
#                     print(ni, nj)

# -------------------------------------------------------

N = 3  # 행
M = 4  # 열
# N 개의 원소를 갖는 0 으로 초기화 된 1차원 배열
arr1 = [0] * N
# 크기가 N * M 이고 0 으로 초기화 된 2차원 배열
arr2 = [[0] * M for _ in range(N)]

# -------------------------------------------------------

# 배열의 합

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 3
# 1 2 3
# 4 5 6
# 7 8 9
s = 0
for i in range(N):
    for j in range(N):
        s += arr[i][j]
print(s)


# 각 행의 합을 구하고 그 중 최대값을 출력해라
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
maxV = 0   # 최대 행의 합
for i in range(N):
    rs = 0  # 행의 합
    for j in range(N):  # i 행의 j열에 접근
        rs += arr[i][j]
    if maxV < rs:
        maxV = rs
print(maxV)

# -------------------------------------------------------

# 대각선의 합 (왼쪽 위에서 오른쪽 아래로)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
s = 0
for i in range(N):
    s += arr[i][i]

# 반대편 대각선 (오른쪽 위에서 왼쪽 아래로)
s = 0
for i in range(N):
    s += arr[i][N-1-i]

# -------------------------------------------------------

# 대각선 양쪽 합
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
s1 = 0
s2 = 0
for i in range(N):
    for j in range(N):
        if i > j:
            s1 += arr[i][j]
        elif i < j:
            s2 += arr[i][j]
print(s1, s2)

s1 = 0
s2 = 0
for i in range(N):
    for j in range(i+1, N):
        s2 += arr[i][j]
        s1 += arr[j][i]
print(s1, s2)

# -------------------------------------------------------

# 사선의 합
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = [0]*(2*N-1)
for i in range(N):
    for j in range(N):
        s[i+j] += arr[i][j]
print(s)

# -------------------------------------------------------

# swea user problem - 9386
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    maxV = 0
    cnt = 0
    for i in range(N):
        if nums[i] == 1:
            cnt += 1
            if maxV < cnt:
                maxV = cnt
        else:
            cnt = 0
    print(f'#{tc} {maxV}')

# -------------------------------------------------------

# swea user problem - 9489
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 행 , M 열
    nums = [list(map(int, input().split())) for _ in range(N)]

    all_max = 0
    for i in range(N):
        max_x = 0
        for j in range(M):
            if nums[i][j] == 1:
                max_x += 1
                if max_x > all_max:
                    all_max = max_x
            else:
                max_x = 0

    for i in range(M):
        max_y = 0
        for j in range(N):
            if nums[j][i] == 1:
                max_y += 1
                if max_y > all_max:
                    all_max = max_y
            else:
                max_y = 0

    print(f'#{tc} {all_max}')