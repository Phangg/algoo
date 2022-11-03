import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('input.txt')

def solve(start, end):
    # 트리에 노드 1개일 경우 리턴
    if start > end:
        return

    # 루트노드보다 큰 숫자가 나올때까지 (오른쪽 트리의 루트 = x)
    root = n_lst[start]
    x = start + 1
    while x <= end:
        if n_lst[x] > root:
            break
        x += 1

    # 왼쪽 트리
    solve(start+1, x-1)
    # 오른쪽 트리
    solve(x, end)
    print(root)

n_lst = []
while 1:
    try:
        node = int(sys.stdin.readline())
        n_lst.append(node)
    except:
        break
# print(n_lst)

solve(0, len(n_lst) - 1)