import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    dump = int(input())
    box_lst = list(map(int, input().split()))

    for d in range(dump):
        box_lst[box_lst.index(max(box_lst))] -= 1
        box_lst[box_lst.index(min(box_lst))] += 1
        if max(box_lst) - min(box_lst) <= 1:
            break

    print(f'#{tc}', max(box_lst)-min(box_lst))


# for n in range(1, 11):
#     cnt = int(input())
#     boxes = list(map(int, input().split()))
#     boxes.sort()
#
#     while cnt > 0:
#         if boxes[0] == boxes[99]:
#             break
#         boxes[0] += 1
#         boxes[99] -= 1
#         boxes.sort()
#         cnt -= 1
#     print(f'#{n} {boxes[99] - boxes[0]}')