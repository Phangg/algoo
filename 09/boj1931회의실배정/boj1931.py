import sys
sys.stdin = open('input.txt')

def start_check():
    s_cnt = 0
    tmp = 0
    for i in range(N):
        if not tmp:
            tmp = e_lst[i][1]
            s_cnt += 1
        elif s_lst[i][0] >= tmp:
            tmp = s_lst[i][1]
            s_cnt += 1
    return s_cnt

def end_check():
    e_cnt = 0
    tmp = 0
    for i in range(N-1, -1, -1):
        if not tmp:
            tmp = e_lst[i][0]
            e_cnt += 1
        elif e_lst[i][1] <= tmp:
            tmp = e_lst[i][0]
            e_cnt += 1
    return e_cnt

N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
s_lst = sorted(lst, key=lambda x: (x[1], x[0]))
e_lst = sorted(lst, key=lambda x: (x[0], x[1]))
# print(s_lst)
# print(e_lst)

x = start_check()
y = end_check()
# print(x)
# print(y)

if x > y:
    print(x)
else:
    print(y)