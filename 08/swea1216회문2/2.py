import sys
sys.stdin = open('input.txt')

def palin(arr):
    for length in range(100, 0, -1):
        for i in range(100):
            for j in range(100-length+1):
                for k in range(length//2):
                    if arr[i][j+k] != arr[i][j+length-1-k]:
                        break
                else:
                    return length

T = 10
for t in range(1, T+1):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    arr_h = list(map(list, zip(*arr)))

    x = palin(arr)
    y = palin(arr_h)
    if x > y:
        print(f'#{tc} {x}')
    else:
        print(f'#{tc} {y}')