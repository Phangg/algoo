import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    poll = list(input())                                    # 리스트로 받기

    total = 0
    p_cnt = 0
    for x in range(len(poll)-1):
        if poll[x] == '(':
            if poll[x+1] == ')':                            # 레이저의 경우 현재 놓인 막대기만큼 막대기가 투가
                total += p_cnt                              # 총 조각 수에 현재 놓인 막대기의 수를 더해줌
            else:
                p_cnt += 1                                  # 막대 추가 / 총 조각 수 추가
                total += 1
        elif poll[x] == ')' and poll[x-1] == ')':           # 레이저가 아닌데 막대가 끝나는 경우
            p_cnt -= 1                                      # 놓여진 막대 한개 줄어드는 것 체크
    print(f'#{tc} {total}')
