import sys
sys.stdin = open('input.txt')

arr = [[0] * 101 for _ in range(101)]               # 좌표는 1이상 100이하

N = 4                                               # 좌표 입력 4줄
for _ in range(N):
    nums = list(map(int, sys.stdin.readline().split()))

    for i in range(nums[0], nums[2]):               # 입력된 좌표에 맞는 값에 1 넣어주기 (합집합이니까)
        for j in range(nums[1], nums[3]):
            arr[i][j] = 1

res = 0
for i in range(101):                                # 배열 돌면서 1 있을때 마다 +1
    for j in range(101):
        if arr[i][j] == 1:
            res += 1

print(res)
