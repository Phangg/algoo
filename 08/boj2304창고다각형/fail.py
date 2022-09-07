import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
dic = {}
for _ in range(N):
    L, H = map(int, sys.stdin.readline().split())
    # print(L, H)
    dic[L] = H

sort_dic = sorted(dic.items())
# print(sort_dic)

max_h = max(dic.values())
# print(max_h)
max_idx = 0
for t in range(N):
    if sort_dic[t][1] == max_h:
        max_idx = t
        break
# print(max_idx)

# 작은 사각형 넓이 구해서 더해주기
# max 전까지
ans_area = 0
h = 0
w = 0
start_w = 0
for i in range(max_idx):
    if sort_dic[i][1] > h:
        h = sort_dic[i][1]
        start_w = sort_dic[i][0]
        # print(h, start_w)
    if sort_dic[i+1][1] > h:
        w = sort_dic[i+1][0] - start_w
        # print(w)
        ans_area += (w * h)

# max 일때
ans_area += max_h

# max 이후로
h = 0
w = 0
start_w = 0
for j in range(N-1, max_idx, -1):
    if sort_dic[j][1] > h:
        h = sort_dic[j][1]
        start_w = sort_dic[j][0]
        # print(h, start_w)
    if sort_dic[j-1][1] > h:
        w = start_w - sort_dic[j-1][0]
        # print(w)
        ans_area += (w * h)

print(ans_area)