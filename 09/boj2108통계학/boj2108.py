import sys
from collections import Counter
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이

print(round(sum(nums)/N))

lst = sorted(nums)
print(lst[len(lst)//2])

nums.sort()
# nums 리스트 하나씩 카운트 해서, 가장 많이 나온 두개 숫자 뽑기
# most_common 하면 튜플 형태로,  /  안하면 딕셔너리처럼 나온다
ans = Counter(nums).most_common(2)
# print(ans)
if len(ans) > 1:
    if ans[0][1] == ans[1][1]:
        print(ans[1][0])
    else:
        print(ans[0][0])
else:
    print(ans[0][0])

print(max(nums) - min(nums))


# lst2 = []
# new_nums = sorted(list(set(nums)))
# # print(new_nums)
# for num in new_nums:
#     lst2.append(nums.count(num))
# # print(lst2)
# ans = []
# for i in lst2:
#     if i == max(lst2):
#         ans.append(new_nums[lst2.index(max(lst2))])
#         lst2[lst2.index(max(lst2))] = 0
# if len(ans) > 1:
#     ans.remove(min(ans))
# print(min(ans))
