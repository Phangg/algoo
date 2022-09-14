import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)    # 재귀의 반복이 1000회 제한 -> 제한을 풀어줌

def dfs(s):
    for t in tree[s]:           # 트리에 연결된 곳(자식노드)에 가서
        if p_node[t] == 0:      # 부모노드 값 없다면
            p_node[t] = s       # 현재 위치 -> 부모노드 값 저장
            dfs(t)              # 자식 노드로 이동해서 반복


N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    i, j = map(int, sys.stdin.readline().split())
    tree[i].append(j)
    tree[j].append(i)
# print(tree)

p_node = [0] * (N+1)            # 부모노드를 저장할 리스트 (노드 1부터 시작)
root = 1                        # 문제에서 루트 노드 1 로 가정
dfs(root)                       # 함수 실행
# print(p_node)

for idx, ans in enumerate(p_node):
    if idx >= 2:                # 2번 노드부터 출력
        print(ans)