import sys
sys.stdin = open('input.txt')

def pre(n):
    if type(tree[n]) == int:
        return tree[n]
    else:
        L = pre(L_ch[n])
        R = pre(R_ch[n])
        if tree[n] == '+':
            return L + R
        elif tree[n] == '-':
            return L - R
        elif tree[n] == '*':
            return L * R
        elif tree[n] == '/':
            return L / R


T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    L_ch = [0] * (N+1)
    R_ch = [0] * (N+1)
    for _ in range(N):
        lst = list(input().split())

        if lst[1].isdigit():
            tree[int(lst[0])] = int(lst[1])
        else:
            tree[int(lst[0])] = lst[1]
            L_ch[int(lst[0])] = int(lst[2])
            R_ch[int(lst[0])] = int(lst[3])
    # print(tree)

    res = round(pre(1))
    print(f'#{tc}', res)
