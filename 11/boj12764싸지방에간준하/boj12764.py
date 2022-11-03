import sys
import heapq
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

# 컴터 끝나는 시간 저장할 리스트
com_lst = [0 for _ in range(n)]
# 컴터 사용 인원 체크 리스트
cnt_lst = [0 for _ in range(n)]

# 인풋 받은 p, q 를 힙큐에 넣기
hq = []
for _ in range(n):
    p, q = map(int, sys.stdin.readline().split())
    heapq.heappush(hq, (p, q))

# 사용되는 컴퓨터 수
used = 0

# 시작 시간이 종료시간 보다 클 때, 끝나는 시간 저장 + 컴터 사용 인원 체크
while hq:
    s, e = heapq.heappop(hq)
    for i in range(len(com_lst)):
        if com_lst[i] == 0 and s == 0:
            used += 1
            com_lst[i] = e
            cnt_lst[i] += 1
            break
        elif com_lst[i] < s:
            if com_lst[i] == 0:
                used += 1
            com_lst[i] = e
            cnt_lst[i] += 1
            break
# print(com_lst)
# print(cnt_lst)

print(used)
for x in cnt_lst:
    if x:
        print(x, end=' ')