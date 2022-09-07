import sys
sys.stdin = open('3input.txt')

N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)

res = 0
while start <= end:
    total = 0
    mid = (start + end)//2
    for i in lst:
        if i > mid:
            total += (i - mid)
    if M <= total:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)
