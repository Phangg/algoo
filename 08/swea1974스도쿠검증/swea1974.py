import sys
sys.stdin = open('input.txt')

def check_line(x):                                  # 2차원 배열 한 줄 같은 번호 있는지 체크
    ans = 1
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(j+1, len(x)):
                if x[i][j] == x[i][k]:
                    ans = 0
                    break
    return ans

N = 9                                   # 9 * 9 크기
T = int(input())
for tc in range(1, T+1):
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst_h = list(map(list, zip(*lst)))                          # 리스트 세로 버전

    res = 1
    for x in range(0, N, 3):
        for y in range(0, N, 3):
            box_lst = []
            for z in range(3):
                for v in range(3):
                    box_lst.append(lst[x+z][y+v])
            for n in range(N):
                for m in range(n+1, N):
                    if box_lst[n] == box_lst[m]:
                        res = 0
                        break

    if check_line(lst) == 1 and check_line(lst_h) == 1 and res == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
