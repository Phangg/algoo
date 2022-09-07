import sys
sys.stdin = open('input.txt')

S = int(sys.stdin.readline())                               # 스위치 개수
s_lst = list(map(int, sys.stdin.readline().split()))        # 스위치 상태 리스트 / 1:ON , 0:OFF
student = int(sys.stdin.readline())                         # 학생 수
for _ in range(student):                                    # sex: 성별 -> 1: 남 , 2: 여
    sex, num = map(int, sys.stdin.readline().split())       # num: 학생이 받은 수 (스위치 개수 이하)

    if sex == 1:                                            # 남자의 경우 num 의 배수 스위치 바꾸기
        for i in range(1, S//num+1):                        # 나누어지는 만큼 체크
            if s_lst[num*i-1] == 1:
                s_lst[num*i-1] = 0
            else:
                s_lst[num*i-1] = 1

    else:                                                   # 여자일 경우
        idx = num - 1                                       # idx 와 리스트 숫자의 차이가 1씩 나서 조정
        if num <= S // 2:                                   # 중간 값이 어느쪽에 가까운지 확인, 가까운쪽 기준 탐색
            for i in range(0, num):                         # 작은쪽에 가까울 경우
                if s_lst[idx-i] == s_lst[idx+i]:
                    if s_lst[idx-i] == 1:
                        s_lst[idx-i] = 0
                        s_lst[idx+i] = 0
                    else:
                        s_lst[idx-i] = 1
                        s_lst[idx+i] = 1
                else:
                    break
        elif num < S:
            for i in range(0, S-num+1):                       # 큰 쪽에 가까울 경우
                if s_lst[idx-i] == s_lst[idx+i]:
                    if s_lst[idx-i] == 1:
                        s_lst[idx-i] = 0
                        s_lst[idx+i] = 0
                    else:
                        s_lst[idx-i] = 1
                        s_lst[idx+i] = 1
                else:
                    break
        else:
            if s_lst[idx] == 0:
                s_lst[idx] = 1
            else:
                s_lst[idx] = 0

for i in range(S):
    print(s_lst[i], end=' ')
    if (i+1) % 20 == 0:
        print()
