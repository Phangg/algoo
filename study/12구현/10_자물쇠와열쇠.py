import copy

def solve(arr, N):
    for i in range(N, N * 2):                       # 가운데 자물쇠 부분 체크
        for j in range(N, N * 2):
            if arr[i][j] != 1:                      # 1이 아닌게 있으면 못열었다는 거니까..
                return 0
    return 1

def check(dummy, key, M, N):
    arr = copy.deepcopy(dummy)                      # 2차원 배열 복사
    for i in range(N * 2):                          # 예를 들면, key 크기가 3이라서 0~6 까지만 체크하는 것
        for j in range(N * 2):
            for x in range(M):
                for y in range(M):                  # arr 위치에 키의 1 값(튀어나온 부분)을 추가
                    arr[i + x][j + y] += key[x][y]
            if solve(arr, N):                       # 이때 변화한 arr 의 자물쇠 부분이 잘 처리 되었는지 solve 함수로 체크
                return 1
            arr = copy.deepcopy(dummy)              # arr 다시 초기화 해주기
    return 0

def solution(key, lock):
    M, N = len(key), len(lock)
    dummy = [[0] * (N * 3) for _ in range(N * 3)]   # 열쇠가 자물쇠 밖으로 나가도 가능.. 더미 만들기
    for i in range(N):
        for j in range(N):                          # 더미 가운데에 자물쇠 위치 시키기
            dummy[i + N][j + N] = lock[i][j]
    # print(dummy)
    for x in range(4):                              # 90도씩 돌려가면서 체크
        if not x:                                   # 처음에는 그냥 하기 위함
            res = check(dummy, key, M, N)
            if res:
                return True
        else:
            key = list(map(list, zip(*key[::-1])))
            res = check(dummy, key, M, N)
            if res:
                return True
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))


