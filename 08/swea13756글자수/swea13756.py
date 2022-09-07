import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = sorted(set(input()))
    str2 = list(input())
    dic_1 = {}
    for i, v in enumerate(str1):
        dic_1[v] = 0
        for j in str2:
            if v == j:
                dic_1[v] += 1
    print(f'#{tc}', max(dic_1.values()))