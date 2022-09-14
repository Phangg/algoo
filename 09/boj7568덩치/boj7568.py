import sys
from collections import defaultdict
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
per_info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(per_info)

ans_dict =defaultdict(int)                  # 기본 값 0 으로 같는 딕셔너리
for idx, i in enumerate(per_info):
    for j in per_info:                      # 자기 자신 제외 / 내가 남보다 작으면 등수 +1
        if (i != j) and (i[0] < j[0]) and (i[1] < j[1]):
            ans_dict[idx] += 1
for man in range(N):                        # 등수는 1부터 시작이니 +1 해서 출력
    print(ans_dict[man]+1, end=' ')