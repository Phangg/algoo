import sys
sys.stdin = open('input.txt')

# N: 몇명? / M: 몇초? / K: 붕어빵 몇개?
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    visit_time_lst = list(map(int, input().split()))
    visit_time_lst.sort()               # 오름차순 정렬
    # print(visit_time_lst)
    ans = 1                             # 1: Possible / 0: Impossible

    bread = 0                           # 지금 만들어진 빵의 개수
    sell = 0                            # 판매된 빵 수량
    for visit in visit_time_lst:
        if visit < M:                   # 오름차순 리스트
            ans = 0                     # 맨 처음 손님 방문 시간이 빵만드는 시간보다 작으면 이미 실패
            break
        else:
            bread = (visit//M) * K      # 빵 개수 계속 초기화해서 생각
            sell -= 1                   # 손님 하나당 빵 개수 -1
            if bread + sell < 0:        # sell 은 음수 -> 빵 보다 판매가 더 많으면, 실패
                ans = 0

    if ans:
        print(f'#{tc}', 'Possible')
    else:
        print(f'#{tc}', 'Impossible')