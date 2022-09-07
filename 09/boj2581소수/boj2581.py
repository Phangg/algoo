import sys
sys.stdin = open('input.txt')

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

nums = set(range(M, N+1))
no_su = set()
for num in range(M, N+1):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            no_su.add(num)
            break
# print(no_su)
if 1 in nums:
    nums.remove(1)

ans = list(nums-no_su)
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(min(ans))