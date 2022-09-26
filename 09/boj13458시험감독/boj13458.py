import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
a_lst = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
# print(a_lst)

b_cnt = 0
c_cnt = 0
for a in a_lst:
    a -= B
    b_cnt += 1
    if a > 0:
        if a % C:
            c_cnt += (a//C + 1)
        else:
            c_cnt += (a//C)
print(b_cnt + c_cnt)
