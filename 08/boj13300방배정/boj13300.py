import sys
sys.stdin = open('input.txt')

# 학년당 몇명인지 체크 / 필요한 방의 개수 반환
def check_room(lst, k):
    room_cnt = 0
    for i in range(1, 7):                           # 1학년부터 6학년까지
        stu_cnt = 0
        for j in range(len(lst)):
            if lst[j][1] == i:                      # 학생 정보에서 학년이 i 와 같을 때
                stu_cnt += 1                        # 각 학년 마다 몇명인지
                if stu_cnt == k:                    # k(한방 인원) 과 같아지면
                    room_cnt += 1                   # 방 개수 +1
                    stu_cnt = 0                     # 학생수 초기화
            if j == len(lst)-1 and stu_cnt:         # 그런거 관계 없이 리스트 다 돌았을때, 학생 카운트 수가 0이 아니라면
                room_cnt += 1                       # 방 +1
    return room_cnt

# N: 수학여행 참가 학생 수 / K: 한반에 배정할 수 있는 최대 인원 수
N, K = map(int, sys.stdin.readline().split())
student_lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(student_lst)

m_lst = []                                          # 남학생 정보 리스트
fm_lst = []                                         # 여학생 정보 리스트
for student in student_lst:
    if student[0]:                                  # 1 -> 남자일때
        m_lst.append(student)
    else:                                           # 0 -> 여자일때
        fm_lst.append(student)
# print(m_lst)
# print(fm_lst)

# print(check_room(m_lst, K))
# print(check_room(fm_lst, K))

room_m = check_room(m_lst, K)
room_fm = check_room(fm_lst, K)

print(room_m + room_fm)
