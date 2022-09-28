import sys
sys.stdin = open('13618input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stop_lst = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            stop_lst[i] += 1
    P = int(input())
    ans = []
    for _ in range(P):
        ans.append(stop_lst[int(input())])
    print(f'#{tc}', *ans)