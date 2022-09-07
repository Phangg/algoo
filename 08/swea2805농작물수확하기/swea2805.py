# 농장 크기 항상 홀수
# 수확은 농장 크기에 딱 맞는 마름모 형태
# 1 <= N <=49
# 농작물 가치 1~5

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())                                            # N : 농장 크기
    farm = [list(map(int, input())) for _ in range(N)]

    # center : 마름모를 가로지르는 가운데 가장 긴 길이를 가지는 idx
    center = N//2

    # 0행부터 중간행 전까지
    ans_area = []                                               # 수확할 범위의 총 수익
    for i in range(center):                                       # N=7을 예로 들면 0,1,2 행만 순회
        ans_area.append(farm[i][(center)-i:(center)+i+1])           # 각 행에 맞는 숫자 만큼 중간 idx 값 앞뒤로 같이 슬라이싱해서 append

    # 중간행 추가
    ans_area.append(farm[center])

    # 중간행부터 -1행까지
    for j in range((center)+1, N):
        ans_area.append(farm[j][(center)+j-N+1:(center)-j+N-1+1])

    res = 0
    for ans in ans_area:
        for a in ans:
            res += a
    print(f'#{tc} {res}')