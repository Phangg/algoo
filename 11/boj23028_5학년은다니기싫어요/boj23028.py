import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
n, a, b = map(int, input().split())
lst = []
for _ in range(10):
    lst.append(list(map(int, input().split())))

left = 8 - n
for i in range(left):
    m, s = lst[i][0], lst[i][1]
    if (m * 3) + a >= 66:
        if (m * 3) + b >= 130:
            print('Nice')
            break
        elif (m * 3) + b < 130:
            if m + s >= 6 and (m * 3) + ((6 - m) * 3) + b >= 130:
                print('Nice')
                break
            elif m + s < 6 and (m * 3) + (s * 3) + b >= 130:
                print('Nice')
                break
    a += (m * 3)
    if m + s >= 6:
        b += (m * 3) + ((6 - m) * 3)
    else:
        b += (m * 3) + (s * 3)
else:
    print('Nae ga wae')