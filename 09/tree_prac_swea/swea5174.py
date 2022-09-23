import sys
sys.stdin = open('5174input.txt')

def node_check(n):                          # 노드 있는지 체크
    global ans
    if n:                                   # n이 0이 아닐경우
        ans += 1
        node_check(L[n])                    # 왼쪽 자식 값 체크
        node_check(R[n])                    # 오른쪽 자식 값 체크
    return ans

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())        # E : 간선 개수 / E + 1 : 노드 개수 / N : 원하는 것은 N밑의 서브 노드 수
    lst = list(map(int, input().split()))
    L = [0] * (E+1+1)                       # 왼쪽 자식 리스트
    R = [0] * (E+1+1)                       # 오른쪽 자식 리스트
    # print(lst)
    for i in range(0, E*2, 2):
        if L[lst[i]] == 0:                  # 왼쪽에 없으면, 왼쪽부터 자식 노드 배정
            L[lst[i]] = lst[i+1]
        else:
            R[lst[i]] = lst[i+1]
    # print(L)
    # print(R)

    ans = 0
    node_check(N)
    print(f'#{tc} {ans}')