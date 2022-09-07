import sys
sys.stdin = open('input.txt')

# 중복 없이 순열 만들기
def p(i, N):
    global idx_lst
    if i == N:
        idx_lst.append(x[:])
    for n in range(N):
        if n not in x[:i]:
            x[i] = n
            p(i+1, N)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    minsum = N * 10
    idx_lst = []
    x = [0] * N
    p(0, N)
    # print(idx_lst)

    sum_lst = []
    for j in range(len(idx_lst)):
        sub_sum = []
        for k in range(N):
            a = idx_lst[j][k]
            if a > minsum:
                break
            else:
                sub_sum.append(lst[k][a])
        if minsum > sum(sub_sum):
            minsum = sum(sub_sum)
    print(f'#{tc}', minsum)