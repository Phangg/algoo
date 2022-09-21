import sys
import heapq
from collections import defaultdict
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())

    hq, rhq = [], []                # hq : 최소힙  /  rhq : 최대힙
    res = 0                         # res : 큐에 남아있는 숫자 개수
    dic = defaultdict(int)

    for _ in range(N):
        order, data = sys.stdin.readline().split()
        data = int(data)

        if order == 'I':
            heapq.heappush(hq, data)
            heapq.heappush(rhq, -data)
            dic[data] += 1
            res += 1

        elif data == -1:                    # -1 일 경우 / 최소힙
            if hq:
                x = heapq.heappop(hq)
                while not dic[x]:               # 최소힙의 값이 0이면
                    try:
                        x = heapq.heappop(hq)   # 다음 최소값을 검색
                    except:
                        hq, rhq = [], []        # 딕셔너리 값 없는 데..? 지울게 없으니까... 비워버려
                        dic[x] += 1             # break 문 이후에 -1 을 복구하기 위해 미리 +1
                        res += 1
                        break
                dic[x] -= 1
                res -= 1

        elif data == 1:                     # 1 일 경우 / 최대힙
            if rhq:
                rx = heapq.heappop(rhq)
                while not dic[-rx]:             # rx는 음수화 되어있으니, 다시 음수화해서 검색
                    try:
                        rx = heapq.heappop(rhq) # 다음 최대값 검색
                    except:
                        hq, rhq = [], []        # 딕셔너리 값 없는 데..? 지울게 없으니까... 비워버려
                        dic[-rx] += 1           # break 문 이후에 -1 을 복구하기 위해 미리 +1
                        res += 1
                        break
                dic[-rx] -= 1
                res -= 1

    if res > 0:                     # 숫자가 남아있다면,
        x, rx = 0, 0                # 초기화
        while 1:
            rx = heapq.heappop(rhq) # 최대값 검색
            if dic[-rx]:            # rx는 음수화 되어있으니, 다시 음수화
                break               # 딕셔너리 값이 1이상 -> ㅇㅋ
        while 1:
            x = heapq.heappop(hq)   # 최소값 검색
            if dic[x]:              # 딕셔너리 값이 1이상 -> ㅇㅋ
                break
        print(-rx, x)               # rx는 음수화 되어있으니, 다시 음수화
    else:
        print('EMPTY')              # 숫자가 남아있지 않다면, (res == 0)
