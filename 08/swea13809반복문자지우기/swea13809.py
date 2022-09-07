import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    S = list(input())

    i = 0
    while i < len(S) - 2 + 1:           # 두개의 연속된 글자를 확인하니까..
        if S[i] == S[i+1]:              # 이거랑 다음거랑 같아?
            S.pop(i)                    # 뽑아
            S.pop(i)                    # 위에서 뽑으면서 뒤에 값들 index가 -1 되었으니, 또 같은 인덱스 뽑아
            i = 0                       # 새로운 리스트로 다시 검색할거니까 i 초기화
        else:
            i += 1                      # 같은 경우 없으면 i 에 1을 더해서 다음 단계로 이동!
    print(f'#{tc}', len(S))