import sys
sys.stdin = open('input.txt')

def check_space(X):

    cnt = 0
    for i in range(N):
        for j in range(N-K+1):
            if j == 0:
                if X[i][j:j+K+1] == [1]*K + [0]:
                    cnt += 1
            elif 0 < j+K < N:
                if X[i][j-1:j+K+1] == [0] + [1]*K + [0]:
                    cnt += 1
            elif j+K == N:
                if X[i][j-1:j+K] == [0] + [1]*K:
                    cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())                           # N*N 배열 / K 단어 길이
    arr = [list(map(int, input().split())) for _ in range(N)]  # 흰색 1 / 검은색 0
    arr_h = list(map(list, zip(*arr)))                         # 각각 튜플이 아닌, 리스트로 받기 위해 map(list, ~~)!!!


    w = check_space(arr)
    h = check_space(arr_h)

    print(f'#{tc}', w+h)
