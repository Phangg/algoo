import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T, L = map(int, input().split())                    # T : 테스트 케이스 번호 / L : 길(간선) 개수
    L_lst = list(map(int, input().split()))             # 총 L * 2 개의 숫자가 들어감
    # print(L_lst)

    lst = [[] for _ in range(100)]                      # 최대 노드의 개수는 100개
    for i in range(L):                                  # 길의 개수만큼
        lst[L_lst[i*2]].append(L_lst[i*2+1])            # 짝수 번호들이 해당 노드(idx) / 뒤에 이어오는 홀수들이 인접 노드 / 단방향
    # print(lst)

    stack = []
    visited = [0] * 100                                 # 방문 시, 체크 / 첫 노드(idx) 0부터 시작이니, 100만큼만
    s, e = 0, 99                                        # 시작 지점 0 / 도착지점은 99라고 주어짐
    stack.append(s)
    visited[0] = 1

    while stack:                                        # 스택이 비워질 때 까지 반복
        s = stack[-1]
        visited[s] = 1                                  # 가는 길 체크
        for i in lst[s]:
            if visited[i] == 0:
                stack.append(i)
                break
        else:
            stack.pop()

    if visited[e] == 1:
        print(f'#{T} 1')
    else:
        print(f'#{T} 0')