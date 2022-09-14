import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    min_idx = M
    for _ in range(M):
        idx, v = map(int, input().split())
        tree[idx] = v
        if idx < min_idx:
            min_idx = idx
    # print(tree)
    if N % 2:
        x = min_idx - 1
    else:
        x = min_idx
    while x >= L:
        if (x * 2 + 1) <= N:
            tree[x] = tree[x*2] + tree[x*2 + 1]
        else:
            tree[x] = tree[x * 2]
        x -= 1

    print(f'#{tc}', tree[L])