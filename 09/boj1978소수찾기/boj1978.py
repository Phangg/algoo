import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
# print(nums)

for num in nums:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            N -= 1
            break
if 1 in nums:
    N -= 1
print(N)