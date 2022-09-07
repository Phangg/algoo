import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())                           # 사람 수
    p_lst = list(map(int, sys.stdin.readline().split()))    # 왼쪽에 나보다 키큰 사람이 몇명 있는지 리스트 / 사람은 1~N번

    ans = [0] * N                                           # 답안용

    for i in range(N):                                      # p_lst 순회용
        cnt = 0                                             # 내 앞에 나보다 큰 숫자를 세어 줄 카운트
        for j in range(N):                                  # ans 순회용
            if ans[j] == 0:                                 # 0 일 경우 -> 내 앞에 사람 체크
                cnt += 1
                if cnt == p_lst[i] + 1:                     # 사람 숫자가 i번 사람 왼쪽 인원 +1 일때 => 인덱스로 위치 할 곳은 +1 이기 때문
                    ans[j] = i + 1                          # 왼쪽에 공간을 두고 위치 => i는 인덱스 / 사람 번호 1번부터라 +1
                    break
    print(*ans)