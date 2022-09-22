import sys
sys.stdin = open('input.txt')
# 1번은 사무실 / 2번부터 N번은 관리구역 번호

def way(i, k):
    global lst
    if i == k:
        if len(nums) == N:                      # 뒤에 1을 넣을 수 있도록 조건 걸기
            nums.append(1)
            lst.append(nums[:])                 # 리스트가 아닌 값을 넣어줘야 함 !!!!
        else:
            lst.append(nums[:])
    else:
        for j in range(i, k):
            nums[i], nums[j] = nums[j], nums[i]
            way(i+1, k)
            nums[j], nums[i] = nums[i], nums[j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    nums = [x for x in range(1, N+1)]
    lst = []
    way(1, N)                                   # 조합 함수 돌기
    # print(lst)

    min_b = N * N * 100
    for tmp in lst:
        res = 0
        for i in range(0, N):
            x, y = tmp[i]-1, tmp[i+1]-1         # 인덱스니까 -1 해서 체크
            res += e[x][y]
        if min_b > res:                         # 최소값 체크
            min_b = res
    print(f'#{tc} {min_b}')
