import sys
sys.stdin = open('25input.txt')

def solution(N, stages):
    answer = []
    length = len(stages)                # 첫 리스트에서 점점 줄어드는 리스트 길이를 체크할 변수

    for i in range(1, N+1):             # 리스트 내에 1 부터 N+1까지 있음
        cnt = stages.count(i)           # 숫자 i 가 몇개 있는지 체크

        if length == 0:                 # 리스트 길이가 0 => 실패율 0
            f_per = 0
        else:
            f_per = cnt / length        # 실패율 = 숫자 개수 / 리스트 길이 ( 대소비교 위해, // 말고 / 로 진행 )

        answer.append((i, f_per))       # 스테이지 번호 와 해당 스테이지 실패율을 튜플로 같이 리스트 삽입
        length -= cnt                   # 카운트 된 숫자만큼 리스트 길이 감소

    answer.sort(key=lambda x : -x[1])   # 실패율 기준으로 내림차순 정렬
    answer = [a[0] for a in answer]     # 스테이지 번호만 뽑아서 다시 리스트 정리

    return answer

for _ in range(2):
    N = int(input())
    stages = list(map(int, input().split()))
    # print(stages)

    print(solution(N, stages))


