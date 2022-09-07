import sys
sys.stdin = open('input.txt')

# 2차원 배열에서 1: N 위로 이동 red / 2: S 아래로 이동 blue

T = 10
for tc in range(1, T+1):
    N = int(input())                                            # 정사각형 한변 길이
    lst = [list(map(int, input().split())) for _ in range(N)]   # 2차원 배열

    cnt = 0                                                     # 카운트
    for j in range(N):
        stack_v = []                                            # 한개 열 담당 스택 / 열마다 초기화
        for i in range(N):                                      # 세로로 2차원 배열 순회
            if lst[i][j] == 1:                                  # 빨간색 만났을 때 스택 비어있다면, 스택에 넣기
                stack_v.append(lst[i][j])
            elif lst[i][j] == 2:                                # 파란색 만났을 때, 맨위가 빨간색이면, 스택에 넣기
                if stack_v and stack_v[-1] == 1:
                    stack_v.append(lst[i][j])
                    cnt += 1                                    # 카운트 + 1

    print(cnt)