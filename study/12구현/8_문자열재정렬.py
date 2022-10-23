import sys
sys.stdin = open('8input.txt')

S = sys.stdin.readline().rstrip()

lst = []
num = 0
for s in S:
    if s.isdigit():
        num += int(s)
    else:
        lst.append(s)
lst.sort()
print(''.join(lst), end='')
print(num)