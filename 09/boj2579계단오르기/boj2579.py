import sys
sys.stdin = open('input.txt')

S = int(input())
lst = [0 for _ in range(301)]       # 계단 포인트
d = [0 for _ in range(301)]         # 내 누적 포인트

for i in range(S):
    lst[i] = int(input())
# print(lst)

d[0] = lst[0]
d[1] = lst[1] + lst[0]
d[2] = max(lst[1] + lst[2], lst[0] + lst[2])
# 1번에서 2번   or   0번에서 2번

# 인덱스 0부터 했어서, S까지 탐색
for x in range(3, S):
    d[x] = max(d[x-3] + lst[x-1] + lst[x], d[x-2] + lst[x])
    # 마지막 계단 필수니까,
    # 마지막 계단 -1 을 밟는 경우 , 마지막 계단 -2 를 밟는 경우 체크
# print(d)
print(d[S-1])