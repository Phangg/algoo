import sys
sys.stdin = open('input.txt')

# 한 층에 W 개의 방 / 총 H 층 / N 번째 손님
T = int(sys.stdin.readline())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    # print(H, W, N)

    # m 은 배정될 호수 / d 는 배정될 층
    m, d = divmod(N, H)

    # 나머지가 0으로 나누어 떨어지면 H와 같은 값으로 설정
    if N % H == 0:
        d = H
        # print(m, d)
        if m // 10:
            print((d*100) + m)
        else:
            print(int(str(d)+'0'+str(m)))
    # 호수는 1호 부터! m 에 +1 해주기
    else:
        m += 1
        # print(m, d)
        if m // 10:
            print((d*100) + m)
        else:
            print(int(str(d)+'0'+str(m)))