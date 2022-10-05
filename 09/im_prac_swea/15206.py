import sys
from collections import defaultdict
sys.stdin = open('15206input.txt')

T = int(input())
for tc in range(1, T+1):
    card = defaultdict(list)
    lst = list(input())

    flag = 1
    for i in range(0, len(lst), 3):
        t = lst[i]
        xy = (int(lst[i+1]))*10 + int(lst[i+2])
        if xy in card[t]:
            flag = 0
            print(f'#{tc}', 'ERROR')
            break
        else:
            card[t].append(xy)
    if flag:
        print(f'#{tc}', end=' ')
        for x in ['S', 'D', 'H', 'C']:
            print(13 - len(card[x]), end=' ')
        print()