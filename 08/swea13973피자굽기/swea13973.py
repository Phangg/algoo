import sys
from collections import deque
sys.stdin = open('input.txt')

# N 개 만큼 피자 들어갈 수 있음
# M 개의 피자 구워야 함
# 치즈 녹으면 꺼내기 -> 녹는 사람부터 꺼냄
# 피자 1번에 넣을 수 있음
# 치즈는 한바퀴 돌때 //2 로 줄어 든다
# 피자 꺼낸 자리에 바로 새로운 피자

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    c_lst = list(map(int, input().split()))
    cq = deque()

    for idx, n in enumerate(range(N), 1):
        cq.append([idx, c_lst[n]])
    # print(cq)

    p = N
    while len(cq) > 1:
        cq[0][1] = cq[0][1]//2
        if cq[0][1] == 0:
            cq.popleft()
            if p < M:
                cq.append([p+1, c_lst[p]])
                p += 1
        else:
            cq.append(cq.popleft())
    print(f'#{tc} {cq[0][0]}')








