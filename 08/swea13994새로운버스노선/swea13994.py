# 삼성시는 버스 노선을 일반, 급행, 광역 급행으로 구분해 새롭게 바꾸려고 한다.
# 모든 정류장은 1번부터 1000번까지의 번호가 부여되어 있으며, 각 노선은 A에서 B번 정류장까지 다음 규칙에 따라 운행한다.
# - 모든 버스는 A번에서 출발해 B번까지 운행하므로, A와 B정류장에는 반드시 정차한다.
# - 일반버스는 A번부터 B번 사이의 모든 정류장에 정차한다.
# - 급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 짝수 번호 정류장에 정차하고, A가 홀수인 경우 A와 B사이의 모든 홀수 번호 정류장에 정차한다.
# - 광역 급행 버스는 A가 짝수인 경우 A와 B 사이의 모든 4의 배수 번호 정류장에, A가 홀수인 경우 A와 B 사이의 3의 배수이면서 10의 배수가 아닌 번호 정류장에 정차한다.
# 버스의 종류와 출발 도착 정류장에 대한 정보가 주어질 때, 최대 몇 개의 노선이 같은 정류장에 정차하는지 알아내는 프로그램을 만들어보자.

import sys
sys.stdin = open('input.txt')

# N: 노선 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    station = [''] * 1001                                               # 정류장 1번부터 시작 / 최대 1000개
    bus_lst = [list(map(int, input().split())) for _ in range(N)]
    # print(bus_lst)
    for bus_type, start, end in bus_lst:
        if bus_type == 1:                                               # 1번 일반 버스 -> 모든 정류장 -> 'x' 표시
            for i in range(start, end+1):
                station[i] += 'x'
        elif bus_type == 2:
            for i in range(start, end+1, 2):                            # 2번 급행 버스 -> 시작 짝수 : 짝수만 / 시작 홀수 : 홀수만 -> 'y' 표시
                station[i] += 'y'
        else:
            if start % 2:
                for i in range(start, end + 1):                         # 3번 광역 급행 버스 -> 홀수 : 3의 배수 + 10의 배수 아닌 정류장 -> 'z' 표시
                    if (i % 3 == 0) and (i % 10):
                        station[i] += 'z'
            else:
                for i in range(start, end + 1):                         # 3번 광역 급행 버스 -> 짝수 : 4의 배수 -> 'z'표시
                    if i % 4 == 0:
                        station[i] += 'z'
    # print(station)

    max_bus = 0
    for bus in station:                                                 # 가장 많은 버스의 기록이 남은 정류장 -> 버스 몇대? -> 출력
        if max_bus < len(bus):
            max_bus = len(bus)
    print(f'#{tc} {max_bus}')