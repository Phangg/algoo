# Heapq
# 최소 힙(Min Heap)의 구조
# 모든 k에 대해 heap[k] <= heap[2*k+1] 또는 heap[k] <= heap[2*k+2] 만족
# 가장 작은 요소가 heap[0]에 위치

import heapq
hq = []

# heapq.heappush(heap, item)
# 힙의 형태를 유지하면서 item 을 push
heapq.heappush(hq, 4)
heapq.heappush(hq, 1)
heapq.heappush(hq, 3)
heapq.heappush(hq, 7)
print(hq)

# heapq.heappop(heap)
# 힙의 형태를 유지하면서 가장 작은 항목을 pop, 반환
# 비어있으면 IndexError 발생
# 반환하지 않고 접근하고 싶다면, heap[0] 활용
print(heapq.heappop(hq))        # 1
print(hq)                       # [3, 4, 7]
print(hq[0])                    # 3
print(hq)                       # [3, 4, 7]

# heapify(x)
# 리스트 x를 선형 시간으로 제자리에서 heap 으로 변환
# 시간복잡도 O(n)
# 새로운 리스트를 반환하는 것이 아니라 인자로 넘긴 리스트에 직접 변경
# 원본 리스트의 형태를 보존해야되는 경우, 해당 리스트를 복제한 후에 인자로 넘겨야 함
x = [4, 3, 1, 2, 5, 6]
print(x)            # [4, 3, 1, 2, 5, 6]
heapq.heapify(x)
print(x)            # [1, 2, 4, 3, 5, 6]

# 최대 힙 ??
# heapq 모듈은 최소 힙(min heap)을 기능만을 동작 -> 작은게 앞으로 감
# 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면,
# 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용
# 각 값에 대한 우선 순위를 구한 후,
# (우선 순위, 값) 구조의 튜플(tuple)을 힙에 추가하거나 삭제
nums = [4, 1, 7, 3, 8, 5]
hq = []
for num in nums:
    heapq.heappush(hq, (-num, num))     # (우선 순위, 값)
print(hq)           # [(-8, 8), (-7, 7), (-5, 5), (-1, 1), (-3, 3), (-4, 4)]
while hq:
    print(heapq.heappop(hq)[1])         # hq 는 튜플 / 튜플의 값을 출력 -> 내림차순으로 하나씩 출력

# 3번째 작은 값 or 3번쨰 큰 값 (인덱스로 작동해서 사실상 4번째)
nums = [4, 1, 7, 3, 8, 5]
heapq.heapify(nums)
print(nums)             # [1, 3, 5, 4, 8, 7]
print(heapq.nlargest(3, [4, 1, 7, 3, 8, 5])[-1])        # 5
print(heapq.nsmallest(3, [4, 1, 7, 3, 8, 5])[-1])       # 4

# heqp sort
def heap_sort(nums):
    hq = []
    for num in nums:
        heapq.heappush(hq, num)                 # heapq 만들기
    sorted_nums = []
    while hq:
        sorted_nums.append(heapq.heappop(hq))   # 제일 작은값 뽑아서 정렬
    return sorted_nums
print(heap_sort([4, 1, 7, 3, 8, 5]))            # [1, 3, 4, 5, 7, 8]
