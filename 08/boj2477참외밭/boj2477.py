import sys
sys.stdin = open('input.txt')

# K : 1m^2 에 자라는 참외 개수
K = int(sys.stdin.readline())

lst = []                                                        # 길이가 순서대로 모두 담긴 리스트
w_lst = []                                                      # 가로 변들의 길이 리스트
h_lst = []                                                      # 세로 변들의 길이 리스트
for _ in range(6):                                              # 육각형
    # 동 1 서 2 남 3 북 4
    position, length = map(int, sys.stdin.readline().split())
    lst.append(length)
    if position == 2 or position == 1:
        h_lst.append(length)
    else:
        w_lst.append(length)

max_h = max(h_lst)                                              # 최대 세로 변 길이
max_w = max(w_lst)                                              # 최대 가로 변 길이
max_h_idx = lst.index(max_h)                                    # 최대 세로 변과 가로 변의 인덱스
max_w_idx = lst.index(max_w)

all_area = max_w * max_h
# 큰 사각형의 넓이

x = abs(lst[max_w_idx-1] - lst[(0 if max_w_idx+1 == 6 else max_w_idx+1)])
# 제일 긴 가로변 양옆에 붙은 세로 변의 길이 차이 / 5일 경우 인덱스 범위 맞춰 줘야 함
y = abs(lst[max_h_idx-1] - lst[(0 if max_h_idx+1 == 6 else max_h_idx+1)])
# 제일 긴 세로변 양옆에 븥은 가로 변의 길이 차이 / 5일 경우 인덱스 범위 맞춰 줘야 함
small_area = x*y
# 패인 부분 (작은 사각형) 의 넓이

print(K*(all_area - small_area))
