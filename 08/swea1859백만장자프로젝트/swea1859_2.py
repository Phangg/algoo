import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    adv = 0
    max_p = prices[-1]                  # 최대 값을 마지막 날 값으로 임시 지정

    for i in range(N-1, -1, -1):        # 뒤에서부터 탐색
        if max_p >= prices[i]:          # 마지막날 가격이 전날보다 크거나 같으면
            adv -= prices[i]            # 총 이익 - 구매
            adv += max_p                # 총 이익 + 최대 값
        elif max_p < prices[i]:
            max_p = prices[i]

    if adv > 0:
        print(f'#{tc} {adv}')
    else:
        print(f'#{tc} 0')
