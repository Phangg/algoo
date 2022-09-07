import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    ans = 0
    for i in range(M-N+1):
        if str2[i:i+N] == str1:
            ans = 1
            break
        else:
            ans = 0
    print(f'#{tc}', ans)