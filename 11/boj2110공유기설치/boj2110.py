import sys
sys.stdin = open('input.txt')

def b_search(s, e):
    while s <= e:
        mid = (s+e) // 2
        c_cnt = 1
        tmp = 0
        for i in range(n):
            if h_lst[i] - h_lst[tmp] >= mid:
                c_cnt += 1
                tmp = i
        if c_cnt < c:
            e = mid - 1
        else:
            s = mid + 1
    return (s+e) // 2


n, c = map(int, sys.stdin.readline().split())
h_lst = sorted(list(int(sys.stdin.readline()) for _ in range(n)))

# 최소 거리 & 최대 거리
min_v = 1
max_v = h_lst[-1] - h_lst[0]
ans = b_search(min_v, max_v)

print(ans)