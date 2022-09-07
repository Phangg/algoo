import sys
sys.stdin = open('input.txt')

def check_palin(X):                         # 회문 판별 함수 설정
    max_len = 0                             # 가장 긴 길이
    for i in range(N):                      # i 행
        for j in range(N):                  # j 열
            for k in range(0, N+1):         # 열 안에서 움직일 범위 설정을 위한 k
                                            # N+1범위? -> k는 인덱스 값으로 k가 100이 되어야 99인덱스까지 탐색 가능
                if X[i][j:k] == X[i][j:k][::-1] and (k-j) > max_len:    # k와 j는 인덱스 값으로 k-j가 문자 길이
                    max_len = (k-j)
    return max_len

T = 10
for _ in range(T):
    tc = int(input())
    N = 100
    arr = [list(input()) for _ in range(N)]
    arr_h = list(zip(*arr))

    w = check_palin(arr)
    h = check_palin(arr_h)
    ans = 0
    if w > h:
        ans = w
    else:
        ans = h
    print(f'#{tc} {ans}')