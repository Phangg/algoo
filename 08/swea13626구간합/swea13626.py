import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    lst = []
    for i in range(0, N-M+1):  # 앞에서 M개씩 더해서 확인 예정
        sum_nums = 0
        for j in range(i, M+i):   # M 개씩 더하기 반복 / 인덱스 N-M 까지
            sum_nums += nums[j]
        lst.append(sum_nums)

        max_sum_nums = lst[0]
        min_sum_nums = lst[0]
        for n in lst:
            if n > max_sum_nums:
                max_sum_nums = n
            if n < min_sum_nums:
                min_sum_nums = n
        result = max_sum_nums - min_sum_nums
    print(f'#{tc} {result}')