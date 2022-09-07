import sys
sys.stdin = open('input.txt')

dif_num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for _ in range(T):
    tc, N = map(str, input().split())
    lst = list(map(str, input().split()))

    ans_lst = []
    for i in range(len(dif_num_lst)):
        for j in lst:
            if j == dif_num_lst[i]:
                ans_lst.append(j)
    print(f'{tc}')
    print(*ans_lst)