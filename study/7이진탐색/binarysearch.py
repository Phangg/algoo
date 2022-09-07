# 이진 탐색
# 전제 조건 -> 데이터 정렬
# 코테에서 탐색 범위가 큰 상황.. ex) 범위가 2000만을 넘어간다면..
# 탐색 범위가 1000만이 넘어가면 O(logN)의 속도룰 내는 알고리즘을 찾아보는 것이..!


def binary_search(array, goal, start, end):
    if start > end:
        return '원소 없음'
    mid = (start + end) // 2
    if array[mid] == goal:
        return mid + 1
    elif goal > array[mid]:
        return binary_search(array, goal, mid + 1, end)
    else:
        return binary_search(array, goal, start, mid - 1)

n, target = 10, 7
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

res = binary_search(arr, target, 0, n-1)
print(res)


print()
#------------------------------------------------------------
def binary_search(array, goal, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == goal:
            return mid
        elif goal > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None

n, target = 10, 7
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

res = binary_search(arr, target, 0, n-1)
if res == None:
    print('원소 없음')
else:
    print(res + 1)