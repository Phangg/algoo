import sys
sys.stdin = open('input.txt')

def where(way, block, w, h):
    if way == 1:
        return[0, block]
    elif way == 2:
        return [h, block]
    elif way == 3:
        return [block, 0]
    else:
        return [block, w]


# w : 블록 가로 길이 / h : 블록 세로 길이 (100이하 자연수)
# s : 상점 개수
# way : 방향 -> 1 북 , 2 남 , 3 서 , 4 동
# block : 몇 블럭 떨어져있는지 -> way 1,2 : 블록의 왼쪽 경계로부터 거리 / way 3,4 : 블록의 위쪽 경계로부터 거리
w, h = map(int, sys.stdin.readline().split())
area = [[0] * (w+1) for _ in range(h+1)]
s = int(sys.stdin.readline())
# s_lst 에 각 상점의 인덱스(좌표) 표기
s_lst = []
for _ in range(s):
    way, block = map(int, sys.stdin.readline().split())
    s_lst.append(where(way, block, w, h))
# print(s_lst)

# 동근이의 위치
d_way, d_block = map(int, sys.stdin.readline().split())
dong_p = where(d_way, d_block, w, h)
# print(dong_p)

length = 0
for store in s_lst:
    if d_way == 1 or d_way == 2:
        if dong_p[0] == store[0]:
            length += abs(store[1] - dong_p[1])
        elif abs(dong_p[0] - store[0]) == h:
            if dong_p[1] != 0 and store[1] != h:
                length += min(dong_p[1]+store[1], abs(w-dong_p[1])+abs(w-store[1])) + h
        elif store[1] == 0 and store[0] != 0 and store[0] != w:
            if d_way == 1:
                length += (dong_p[1] + store[0])
            else:
                length += (dong_p[1] + h - store[0])
        elif store[1] == w and store[0] != 0 and store[0] != w:
            if d_way == 1:
                length += ((w - dong_p[1]) + store[0])
            else:
                length += ((w - dong_p[1]) + h - store[0])

    elif d_way == 3 or d_way == 4:
        if dong_p[1] == store[1]:
            length += abs(store[0] - dong_p[0])
        elif abs(dong_p[1] - store[1]) == w:
            if dong_p[0] != 0 and store[0] != w:
                length += (min((dong_p[0]+store[0]), (abs(h-dong_p[0])+abs(h-store[0]))) + w)
        elif store[0] == 0 and store[1] != 0 and store[1] != h:
            if d_way == 3:
                length += (dong_p[0] + store[1])
            else:
                length += (dong_p[0] + w - store[1])
        elif store[0] == h and store[1] != 0 and store[1] != h:
            if d_way == 3:
                length += ((h - dong_p[0]) + store[1])
            else:
                length += ((h - dong_p[0]) + h - store[1])

print(length)