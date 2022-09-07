import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(1, N):                        # 삽입 정렬
        while nums[i-1] > nums[i] and i > 0:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            i -= 1
    print(f'#{tc}', end=' ')                     # tc 와 답안을 이어 붙이기
    print(*nums)
