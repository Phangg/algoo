import sys
sys.stdin = open('input.txt')

def my_sum(X_lst):
    m_sum = 0
    for x in X_lst:
        m_sum += x
    return m_sum

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N 부분 집합 원소 개수 / K 부분 집합의 합
    num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    len_n = len(num_lst)

    all_lst = []
    for i in range(1 << len_n):
        lst = []
        for j in range(len_n):
            if i & (1 << j):
                lst.append(num_lst[j])
        all_lst.append(lst)

    same_len_lst = []
    for a in all_lst:
        if len(a) == N:
            same_len_lst.append(a)

    cnt = 0
    for s in same_len_lst:
        if my_sum(s) == K:
            cnt += 1
    print(f'#{tc} {cnt}')
