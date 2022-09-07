# 주사위 -> A F / C E / B D 끼리 마주 봄
# 리스트 순서 A B C D E F
# 1번 주사위를 자유롭게 시작
# 1번 주사위 윗면 = 2번 아랫면 / 2번 윗면 = 3번 아랫면 ...
# 주사위 쌓고 나서, 위 아래 고정 된 상태 / 옆면 각각 돌려서 기둥 옆 부분 한 면의 최대 합 만들기

import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                                           # N : 주사위의 개수
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 2차원 배열로 받기
# print(nums)

