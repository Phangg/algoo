import sys
sys.stdin = open('input.txt')

def bfs(v, N, t):                                       # v : 시작 / N : 마지막 노드 / t: 찾는 노드
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:
            return 1                                    # 목표 노드 발견
        for w in lst[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0

for _ in range(10):
    T, L = map(int, input().split())                    # T : 테스트 케이스 번호 / L : 길(간선) 개수
    L_lst = list(map(int, input().split()))             # 총 L * 2 개의 숫자가 들어감
    # print(L_lst)

    lst = [[] for _ in range(100)]                      # 최대 노드의 개수는 100개
    for i in range(L):                                  # 길의 개수만큼
        lst[L_lst[i*2]].append(L_lst[i*2+1])            # 짝수 번호들이 해당 노드(idx) / 뒤에 이어오는 홀수들이 인접 노드 / 단방향
    # print(lst)

    print(f'#{T} {bfs(0, 99, 99)}')