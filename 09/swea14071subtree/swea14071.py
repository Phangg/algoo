import sys
sys.stdin = open('input.txt')

def check(n):
    global cnt
    if n:
        cnt += 1
        check(L_ch[n])
        check(R_ch[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = list(range(E+1))
    # print(tree)
    L_ch = [0] * (E+1+1)
    R_ch = [0] * (E+1+1)
    lst = list(map(int, input().split()))
    # print(lst)
    for i in range(0, 2*E, 2):
        if L_ch[lst[i]] == 0:
            L_ch[lst[i]] = lst[i+1]
        else:
            R_ch[lst[i]] = lst[i+1]
    # print(L_ch)
    # print(R_ch)

    cnt = 0
    check(N)
    print(f'#{tc} {cnt}')