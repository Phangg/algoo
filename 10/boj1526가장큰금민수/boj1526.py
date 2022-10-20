import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

while 1:
    flag = 1
    for i in str(N):
        if i != '4' and i != '7':
            N -= 1
            flag = 0
            break
    if flag:
        print(N)
        break
