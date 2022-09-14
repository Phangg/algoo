
# 최대 힙

def enq(n):
    global last
    last += 1                       # 마지막 노드 추가
    heap[last] = n                  # 마지막 정점에 key 추가

    c = last
    p = c // 2                      # 완전 이진 트리 => 부모 노드 번호 c//2
    while p and heap[p] < heap[c]:  # 부모가 있고, 부모 < 자식  경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = heap[1]                   # 루트 백업
    heap[1] = heap[last]            # 삭제 할 노드의 키를 루트에 복사
    last -= 1                       # 마지막 노드 삭제
    p = 1                           # 루트에 옮긴 값을 자식과 비교
    c = p * 2                       # 왼쪽 자식
    while c <= last:                # 자식이 하나라도 있으면
        if ((c+1) <= last) and (heap[c] < heap[c+1]):      # 오른쪽 자식도 있고, 오른쪽 자식이 더 크면
            c += 1                                         # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:       # 자식이 더 크면 최대합 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c                   # 자식을 새로운 부모로
            c = p * 2               # 왼쪽 자식 번호를 계산
        else:                       # 부모가 더 크면
            break
    return tmp


heap = [0] * 100
last = 0

enq(2)          # 루트에 2
enq(5)          # 2번에 5 -> 1번의 2보다 5가 크니까 교체
enq(7)          # 3번에 7 -> 1번의 5보다 7이 크니까 교체
enq(3)          # 4번에 3 -> 2번의 2보다 3이 크니까 교체
enq(4)          # 5번에 4 -> 2번의 3보다 4가 크니까 교체
enq(6)          # 6번에 6 -> 3번의 5보다 6이 크니까 교체   =>         7
while last:                         #                        4       6
    print(deq())                    #                     2   3    5
