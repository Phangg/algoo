import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    lst = [l for l in range(1, n+1)]    # 0 층 / 1호부터 있음
    # print(lst)
    for i in range(k):                  # 층 돌기
        temp = []
        for j in range(n):              # 호수
            temp.append(sum(lst[:j+1])) # n호 까지 더한 인원
        lst = temp[:]                   # 현재 층 인원으로 체인지
    print(lst[n-1])