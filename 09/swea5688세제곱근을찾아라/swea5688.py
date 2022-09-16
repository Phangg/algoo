import sys
import math
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = round(N**(1/3), 2)
    # print(x)
    if math.ceil(x) == int(x):
        print(f'#{tc}', int(x))
    else:
        print(f'#{tc}', -1)