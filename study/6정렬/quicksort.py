arr = [5, 7, 9, 0, 3, 1, 6, 2, 4]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(arr))

# 시간 복잡도 O(NlogN)
# 숫자를 교환하기 위한 기준 -> pivot
# 분할이 이루어지는 횟수가 기하급수적으로 감소
# 다른 정렬들은 보통 '이미 데이터가 어느정도 정렬' 되어있다면 빠르지만, 퀵은 그런 경우 오히려 느려짐
