import sys
sys.stdin = open('input.txt')

def inorder(n):
    if n <= N:
        inorder(2*n)
        print(ans[n], end='')
        inorder(2*n+1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    ans = [0] * (N+1)
    for i in range(N):
        n_info = list(input().split())
        ans[i+1] = n_info[1]
    print(f'#{tc}', end=' ')
    inorder(1)
    print()