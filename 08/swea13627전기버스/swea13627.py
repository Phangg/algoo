import sys
sys.stdin = open('input.txt')

# K = 1회 충전 시 이동 가능 정류장 수
# N = 0번부터 N 번까지 정류장
# M = 충전기가 설치된 정류장 개수

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    m_lst = list(map(int, input().split()))

    charge = 0
    location = 0
    while location < N:   # 현재 위치가 총 길이 보다 크지 않을 때 까지
        for i in range(location + K, location, -1):   # 최대한 갈 수 있는 만큼 가서 돌아오는 방식
            if i >= N:
                location = N
                break
            elif i in m_lst:    # i가 충전소면  충전 + 위치 재설정 / 충전소 아니면 i가 하나씩 줄면서 확인
                location = i
                charge += 1
                break
        else:    # i가 if, elif 문에 부적합하여 반복 중 for 문의 range 를 벗어나게 될 경우 (충전 실패 경우)
            charge = 0
            break

    print(f'#{tc} {charge}')


