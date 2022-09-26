import sys
sys.stdin = open('input.txt')

def nope(n):
    p_node[n] = 'x'                 # 해당 노드 체크
    for i in range(N):              # 순회
        if p_node[i] == n:          # 해당 노드를 부모로 갖는 노드가 있다면
            nope(i)                 # 그 노드를 가지고 재귀

N = int(sys.stdin.readline())
p_node = list(map(int, sys.stdin.readline().split()))
delete_node = int(sys.stdin.readline())

nope(delete_node)
# print(p_node)

ans = 0
for x in range(N):
    if (type(p_node[x]) == int) and (x not in p_node):      # 삭제 된 노드를 'x'로 바꿨으니 int 만 체크
        ans += 1                                            # 리스트에 없는 숫자만 (리스트에는 부모노드니깐..)
print(ans)