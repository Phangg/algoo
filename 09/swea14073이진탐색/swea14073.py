import sys
sys.stdin = open('input.txt')

def inorder(n):
    global num
    if n < N+1:
        inorder(n*2)
        num += 1
        ans[n] = num
        inorder(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    num = 0
    ans = [0] * (N+1)

    inorder(1)
    # print(ans)
    print(f'#{tc}', ans[1], ans[N//2])