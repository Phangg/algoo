import sys
sys.stdin = open('28input.txt')

# 처음에는 함수로 안하고 했는데, while 문 안에서 O(logN) 만들다가 좀 헷갈려서 걍 함수로 바꿈

def check(s, e, lst):
    if s > e:
        return
    mid = (s + e)//2
    if lst[mid] == mid:                 # 리스트에서 인덱스(mid)와 그 해당 인덱스 값이 같을 때
        return mid
    elif lst[mid] > mid:
        return check(s, mid - 1, lst)
    else:
        return check(mid + 1, e, lst)


T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    ans = check(0, N-1, nums)
    if ans:
        print(ans)
    else:
        print(-1)