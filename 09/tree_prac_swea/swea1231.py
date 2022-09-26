import sys
sys.stdin = open('1231input.txt')

def inorder(n):
    if n < N+1:
        inorder(2*n)
        ans.append(tree[n])
        inorder(2*n+1)

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [''] * (N+1)
    for _ in range(N):
        n_info = list(input().split())
        tree[int(n_info[0])] = n_info[1]

    ans = []
    inorder(1)
    print(f'#{tc}', ''.join(ans))