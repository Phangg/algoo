import sys
sys.stdin = open('27input.txt')

# x 의 시작 지점 찾기
def s_point(L, goal, lst):
    s = 0
    e = L-1
    while s <= e:
        mid = (s + e)//2
        if (mid > 0) and (lst[mid] == goal) and (lst[mid-1] < goal):
            return mid
        elif (mid == 0) and (lst[mid] == goal):
            return mid
        elif lst[mid] >= goal:
            e = mid - 1
        else:
            s = mid + 1
    return -1
# x 의 마지막 지점 찾기
def e_point(L, goal, lst):
    s = 0
    e = L-1
    while s <= e:
        mid = (s + e)//2
        if (mid < L-1) and (lst[mid] == goal) and (lst[mid+1] > goal):
            return mid
        elif (mid == L-1) and (lst[mid] == goal):
            return mid
        elif lst[mid] > goal:
            e = mid - 1
        else:
            s = mid + 1
    return -1

T = int(input())
for _ in range(T):
    N, x = map(int, input().split())
    nums = list(map(int, input().split()))

    # print(s_point(N, x, nums))
    # print(e_point(N, x, nums))

# x 개수 세기
    s_idx = s_point(N, x, nums)
    e_idx = e_point(N, x, nums)

    if s_idx != -1:                     # 둘중 하나만 -1 확인해도 됨
        print(e_idx - s_idx + 1)        # 개수는 종료지점 - 시작지점 + 1
    else:
        print(-1)