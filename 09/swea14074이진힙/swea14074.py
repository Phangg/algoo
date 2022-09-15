import sys
sys.stdin = open('input.txt')

def check(n, c):
    heap[c] = n                               # 값을 넣어주기
    p = c // 2                                # 부모 노드 인덱스
    while n < heap[p]:                          # 부모노드 값보다, 현재 노드 값이 작은 동안
        heap[c], heap[p] = heap[p], heap[c] # 서로 바꿔주기
        c = p                                 # 위로 올라가면서 체크
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = [0] * (N+1)          # 새로 정렬 할 리스트
    # print(lst)

    idx = 1
    for num in lst:             # 노드 1부터니까 ~
        check(num, idx)         # 노드 idx 랑 값을 같이 함수로 보내기
        idx += 1                # idx 증가

    idx = N // 2
    res = 0
    while idx >= 1:
        res += heap[idx]
        idx //= 2
    print(f'#{tc} {res}')