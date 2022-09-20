import sys
sys.stdin = open('input.txt')

def b_num(n):
    ans = [0, 0, 0, 0]
    i = 4-1
    while n > 1:
        ans[i] = str(n % 2)
        n //= 2
        i -= 1
    ans[i] = str(n)
    return ans

x_dic = {'A': 10, 'B': 11, 'C': 12,
         'D': 13, 'E': 14, 'F': 15}

T = int(input())
for tc in range(1, T+1):
    N, x_num = input().split()
    N = int(N)

    B = []

    for idx, char in enumerate(x_num):
        if char in x_dic.keys():
            B += b_num(x_dic[char])
        else:
            B += b_num(int(char))

    print(f'#{tc}', end=' ')
    for a in B:
        print(a, end='')
    print()


#1 0100 0111 1111 1110
#2 0111 1001 1110 0001 0010
#3 0100 0001 1101 1010 0001 0110 1100 1101