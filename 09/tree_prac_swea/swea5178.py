import sys
sys.stdin = open('5178input.txt')

def preorder(n):
    global ans
    if n < (N + 1):
        ans += tree[n]
        preorder(n*2)
        preorder(n*2+1)


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())     # N: 노드 수 / M: 리프노드 수 / L: 출력할 노드 번호
    tree = [0] * (N + 1)
    for _ in range(M):
        leaf, num = map(int, input().split())   # leaf: 리프노드 번호 / num: 자연수
        tree[leaf] = num
    ans = 0
    # print(tree)

    preorder(L)
    print(f'#{tc} {ans}')