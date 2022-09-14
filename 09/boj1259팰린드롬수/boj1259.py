import sys
sys.stdin = open('input.txt')

while 1:
    num = sys.stdin.readline().rstrip()
    if num == '0':
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')
