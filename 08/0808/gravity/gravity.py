# 오른쪽으로 돌리고 떨어지는 건 현재에서 오른쪽으로 가는 것과 동일
# 오른쪽에 나보다 작은 수를 체크

import sys

sys.stdin = open('input.txt')

lst = list(map(int, input().split()))

result = 0
for idx in range(len(lst)):
    value = lst[idx]
    cnt = 0
    for right_idx in range(idx+1, len(lst)):
        if value > lst[right_idx]:
            cnt += 1
    if cnt > result:
        result = cnt

print(result)