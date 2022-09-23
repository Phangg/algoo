import sys
sys.stdin = open('5176input.txt')

def inorder(n):
    global num
    if n < N+1:
        inorder(n*2)
        ans[n] = num
        num += 1
        inorder(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())                # N : 노드의 개수

    num = 1
    ans = [0] * (N+1)
    inorder(1)

    print(f'#{tc}', ans[1], ans[N//2])