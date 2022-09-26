import sys
sys.stdin = open('11315input.txt')

def check1():
    global ans
    for lst in arr:
        for i in range(N - 5 + 1):
            if lst[i:i+5].count('o') == 5:
                ans = True
                return ans

def check2():
    global ans
    for lst in r_arr:
        for i in range(N - 5 + 1):
            if lst[i:i+5].count('o') == 5:
                ans = True
                return ans

def check3():
    global ans
    for i in range(N-5+1):
        for j in range(N-5+1):
            cnt = 0
            for k in range(5):
                if arr[i+k][j+k] == 'o':
                    cnt += 1
                    if cnt == 5:
                        ans = True
                        return ans

def check4():
    global ans
    for i in range(N-5+1):
        for j in range(N-5+1):
            cnt = 0
            for k in range(5):
                if r_arr[i+k][j+k] == 'o':
                    cnt += 1
                    if cnt == 5:
                        ans = True
                        return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    r_arr = list(zip(*arr[::-1]))
    # print(arr)

    ans = False
    check1()
    check2()
    check3()
    check4()
    if ans:
        print(f'#{tc}', 'YES')
    else:
        print(f'#{tc}', 'NO')
