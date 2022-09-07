import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    b_lst = list(map(int, input().split()))

    ans = 0
    for i in range(2, N-2):
        if b_lst[i] == max(b_lst[i-2:i+3]):
            ans += (b_lst[i] - max(max(b_lst[i-2:i]), max(b_lst[i+1:i+3])))

    print(f'#{tc} {ans}')