# 우선 순위 큐 자료구조
# heapq
# 내부적으로 heap 모듈을 사용하는 PriorityQueue 클래스의
# put(), get() 함수는 O(log n)의 시간 복잡도 를 가짐


# queue 내장 모듈로 사용
from queue import PriorityQueue

q = PriorityQueue()

# 우선순위 큐의 디폴트 사이즈는 무한대
# 만약에 특정 최대 크기를 가진 우선순위 큐가 필요하다면 maxsize 를 넘기면 됨
# q = PriorityQueue(maxsize=8)

# 클래스의 put() 메서드를 이용하여 우선순위 큐에 원소를 추가
q.put(4)
q.put(1)
q.put(7)
q.put(3)

# get() 메서드를 이용하여 우선순위 큐에 원소를 삭제
print(q.get())      # 1
print(q.get())      # 3
print(q.get())      # 4
print(q.get())      # 7

# 단순 오름차순이 아닌 다른 기준으로 원소가 정렬되기를 원한다면,
# (우선순위, 값)의 튜플의 형태로 데이터를 추가하고 제거
q.put((3, 'Apple'))
q.put((1, 'Banana'))
q.put((2, 'Cherry'))

print(q.get()[1])       # Banana
print(q.get()[1])       # Cherry
print(q.get()[1])       # Apple