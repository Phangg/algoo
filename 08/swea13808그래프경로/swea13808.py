import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())            # V : 노드 수 / E : 간선 수
    dic = dict()
    for _ in range(E):                          # 딕셔너리 -> key : 노드 / value : 키 노드의 인접 노드
        x, y = map(int, input().split())
        dic[x] = dic.get(x, []) + [y]

    S, G = map(int, input().split())            # S : 출발 지점 / G : 종료 지점

    visited = [0] * (V + 1)                     # 지나간 지역
    stack = [S]

    while stack:                                # 스택이 비어있을 때 까지
        S = stack[-1]                           # top 위치 다시 체크
        visited[S] = 1                          # 현 위치 지나감 표시
        if dic.get(S):                          # .get()을 통해서, error 피하기 (모든 숫자를 키로 가지지 않아서)
            for i in dic.get(S):
                if visited[i] == 0:             # 지나간 적이 없으면~
                    stack.append(i)
                    break
            else:
                stack.pop()
        else:
            stack.pop()

    if visited[G] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')