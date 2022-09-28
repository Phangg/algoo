import sys
sys.stdin = open('15003input.txt')

T = int(input())
for tc in range(1, T+1):
    m_og = list(map(int, input()))
    N = len(m_og)
    start_m = [0] * N
    cnt = 0
    for i in range(N):
        if m_og[i] != start_m[i]:
            if start_m[i]:
                start_m[i:] = [0] * (N-i)
            else:
                start_m[i:] = [1] * (N-i)
            cnt += 1
            if start_m == m_og:
                break
    print(f'#{tc} {cnt}')