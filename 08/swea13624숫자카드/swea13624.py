import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input()))

    lst = [0] * 10
    for i in range(0, len(num)):
        lst[num[i]] += 1
        max_m = 0  # 가장 큰 반복 수
        max_n = 0  # 큰 숫자
        for j in range(0, len(lst)):
            if lst[j] >= max_m:
                max_m = lst[j]
                max_n = j

    print(f'#{tc} {max_n} {max_m}')