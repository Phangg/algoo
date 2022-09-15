import sys
sys.stdin = open('input.txt')

def preorder(n):
    global ans
    if n < (N+1):
        ans += tree[n]
        preorder(2*n)
        preorder(2*n+1)


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    min_idx = M
    for _ in range(M):
        idx, v = map(int, input().split())
        tree[idx] = v

    ans = 0
    preorder(L)
    print(f'#{tc} {ans}')
