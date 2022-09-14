import sys
from collections import defaultdict
sys.stdin = open('input.txt')


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    dic = defaultdict(list)
    for i in range(n):
        w, k = map(str, sys.stdin.readline().split())
        dic[k].append(w)
    # print(dic)

    cnt = 1
    for d in dic:
        cnt *= (len(dic[d]) + 1)            # 의상을 입어도 되고 안입어도 됨
    print(cnt-1)                            # 하나도 안입는 경우가 있으니 -1
