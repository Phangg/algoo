import sys
sys.stdin = open('input.txt')

modify = list(sys.stdin.readline().split('-'))
# print(modify)

nums = []
for m in modify:
    tmp = m.split('+')
    x = 0
    for n in tmp:
        x += int(n)
    nums.append(x)
# print(nums)

ans = nums[0]
for i in range(1, len(nums)):
    ans -= nums[i]
print(ans)