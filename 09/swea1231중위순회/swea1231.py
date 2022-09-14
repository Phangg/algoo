import sys
sys.stdin = open('input.txt')

def inorder(n):
    global ans
    if n:
        inorder(L_ch[n])
        ans.append(n)
        inorder(R_ch[n])

T = 10
for tc in range(1, T+1):
    N = int(input())
    n_num, n_char = [], []
    L_ch = [0] * (N+1)
    R_ch = [0] * (N+1)
    for _ in range(N):
        n_info = input().split()        # n_num, n_char, L_ch, R_ch
        # print(n_info)
        n_num.append(int(n_info[0]))
        n_char.append(n_info[1])
        if len(n_info) == 3:
            L_ch[int(n_info[0])] = int(n_info[2])
        elif len(n_info) == 4:
            L_ch[int(n_info[0])] = int(n_info[2])
            R_ch[int(n_info[0])] = int(n_info[3])
    # print(n_num, n_char, L_ch, R_ch)

    ans = []
    inorder(1)
    print(f'#{tc}', end=' ')
    for a in ans:
        print(n_char[a-1], end='')
    print()