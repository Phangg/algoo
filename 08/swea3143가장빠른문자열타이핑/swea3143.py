import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()  # A text / B pattern

    t_cnt = 0  # 총 타이핑 수
    sub_type = 0  # B를 포함한 횟수 * B 길이
    i = 0
    while i < len(A)-len(B)+1:
        if A[i:i+len(B)] == B:
            sub_type += (len(B)-1)  # (B 길이 -1) 만큼 출력 횟수가 줄어드니까!
            t_cnt = len(A) - sub_type
            i += (len(B)-1)  # pattern 의 길이는 제외하고 재검색을 해야하니까?
        i += 1
    print(f'#{tc} {t_cnt}')