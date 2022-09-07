import sys
sys.stdin = open('input.txt')
                                                # 리스트 길이를 점차 줄여가며, 진행 예정
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))    # 금액 리스트로 받기

    adv = 0                                     # 총 이익
    while len(prices) > 0:                      # 리스트 길이가 0이 되기 전까지
        max_p = 0                               # 최대 값 구하기
        max_idx = 0                             # 최대 값 인덱스 변수 따로 설정
        for j in range(len(prices)):
            if prices[j] > max_p:
                max_p = prices[j]
                max_idx = j

        for i in range(max_idx):               # 리스트 최대값(판매 시점) 인덱스 전까지 회문(구매)
            adv -= prices[i]                   # 총 이익 - 구매 금액
            adv += max_p                       # 구매 1번 할 때, 최대값(판매가) 한번씩 더해주기

        prices = prices[max_idx+1:]            # 리스트 슬라이싱 -> 최대값(판매가) 이후부터 끝까지 리스트 초기화

    if adv <= 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {adv}')