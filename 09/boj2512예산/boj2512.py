import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))    # 예산 리스트
# print(m_lst)
M = int(sys.stdin.readline())                           # 총 예산

s = 1
e = max(m_lst)                  # 예산 중 가장 큰 값 -> 상한액 이하 예산요청? -> 요청한 금액 그대로 배정
while s <= e:
    mid = (s + e)//2
    x = 0
    for m in m_lst:
        if m > mid:             # 상한액 이상 예산요청? -> mid 값으로 배정
            x += mid
        else:                   # 상한액 이하 예산요청? -> 요청한 금액 그대로 배정
            x += m
    if x > M:
        e = mid - 1
    else:
        s = mid + 1
print(e)