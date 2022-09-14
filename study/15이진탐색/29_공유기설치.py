import sys
sys.stdin = open('29input.txt')

def check(minn, maxx, lst):
    while minn <= maxx:
        mid = (minn + maxx) // 2
        point = lst[0]                      # 비교 지점
        machine = 1                         # 공유기 대수
        for i in range(1, N):               # 시작지점 제외 비교
            if (lst[i] - point) >= mid:     # 거리가 mid 보다 크거나 같으면
                point = lst[i]              # 비교 지점 이동
                machine += 1                # 공유기 + 1
        if machine < C:
            maxx = mid - 1
        else:
            minn = mid + 1
    return maxx


N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
# print(house)
house.sort()                        # 정렬
min_len = 1                         # 최소 거리
max_len = house[-1] - house[0]      # 최대 거리


res = check(min_len, max_len, house)
print(res)