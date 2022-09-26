import sys
sys.stdin = open('1232input.txt')

def preorder(n):
    if type(tree[n]) == int:
        return tree[n]
    else:
        L = preorder(L_ch[n])
        R = preorder(R_ch[n])
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
        node_info = list(input().split())
        if len(node_info) == 4:
            tree[int(node_info[0])] = node_info[1]
            L_ch[int(node_info[0])] = int(node_info[2])
            R_ch[int(node_info[0])] = int(node_info[3])
        else:
            tree[int(node_info[0])] = int(node_info[1])

    print(f'#{tc}', int(preorder(1)))