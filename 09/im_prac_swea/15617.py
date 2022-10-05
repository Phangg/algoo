import sys
sys.stdin = open('15617input.txt')

N = int(input())

for x in range(1, N+1):
    tmp = str(x).count('3') + str(x).count('6') + str(x).count('9')
    if tmp:
        print('-'*tmp, end=' ')
    else:
        print(x, end=' ')