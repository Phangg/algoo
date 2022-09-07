import sys
sys.stdin = open('input.txt')

N, M = list(map(int, sys.stdin.readline().split()))

ans = 1
for _ in range(M):
    k = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    if nums != sorted(nums, reverse=True):
        ans = 0
        break

if ans == 1:
    print('Yes')
else:
    print('No')




# all_num_lst = []
# num_lst = []
# for _ in range(M):
#     k = int(sys.stdin.readline())
#     nums = list(map(int, sys.stdin.readline().split()))
#     num_lst.append(nums)
#     all_num_lst += nums
#
# stack = []
# ans = 0
# while len(all_num_lst) > 0:
#     for x in range(M):
#         if len(num_lst[x]) > 0:
#             if min(all_num_lst) != num_lst[x][-1]:
#                 ans = 0
#                 break
#             else:
#                 stack.append(num_lst[x][-1])
#                 num_lst[x].pop(-1)
#                 all_num_lst.remove(min(all_num_lst))
#                 ans = 1
#
# if ans == 1:
#     print('Yes')
# else:
#     print('No')