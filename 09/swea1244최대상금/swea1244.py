import sys
sys.stdin = open('input.txt')

def get_num():
    ret = 0
    for val in nums:
        ret = ret * 10 + val
    return ret

def find_max(k):
    global ans
    val = get_num()
    if val in visit[k]: return
    visit[k].add(val)

    if k == cnt:
        ans = max(ans, val)
    else:
        for i in range(N - 1):
            for j in range(i + 1, N):
                nums[i], nums[j] = nums[j], nums[i]
                find_max(k + 1)
                nums[i], nums[j] = nums[j], nums[i]

for tc in range(1, int(input()) + 1):
    num_str, cnt = input().split()
    N = len(num_str)
    nums = list(map(int, num_str))
    cnt = int(cnt)
    ans = 0
    visit = [set() for _ in range(cnt + 1)]
    find_max(0)
    print(ans)
