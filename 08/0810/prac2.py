import sys
sys.stdin = open('prac2_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = len(arr)  # arr 길이 변수 저장

    nums_lst = []
    for i in range(1 << N):  # 1<<n -> 부분 집합의 개수
        sub_lst = []
        for j in range(N):  # arr 원소 길이 만큼 비교
            if i & (1 << j):  # i 의 j 번 비트가 1 인 경우
                sub_lst.append(arr[j])
        nums_lst.append(sub_lst)

    ans = 0
    for x in range(1, len(nums_lst)):
        if sum(nums_lst[x]) == 0:
            ans = 1
            break

    if ans:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)