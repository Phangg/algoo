'''
정점 번호  V = 1~(E+1)
간선 수  E
부모-자식 순
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:             # 부모가 없으면 root
            return i

def preorder(n):            # 전위 순회
    global cnt
    if n:
        cnt += 1
        # print(n, end=' ')            # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):             # 중위 순회
    global ans
    if n:
        inorder(ch1[n])
        ans = n
        # print(n, end=' ')            # visit(n)
        inorder(ch2[n])

def postorder(n):           # 후위 순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')            # visit(n)


V = int(input())                        # 노드 개수, 마지막 노드 번호
arr = list(map(int, input().split()))
E = V - 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

# 자식을 인덱스로 부모 번호 저장
par = [0]*(V+1)

# for j in range(0, E*2, 2):
#     p, c = arr[j], arr[j+1]
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:             # 자식이 없으면
        ch1[p] = c              # 자식 1로 저장
    else:
        ch2[p] = c

    par[c] = p

print(ch1)
print(ch2)

root = find_root(V)
print(root)
print()

# preorder(root)
# print()

# inorder(root)
# print()

postorder(root)
print()

cnt = 0                 # 3을 루트노트로 했을 때, 순회한 모든 노드의 개수
preorder(3)
print(cnt)
print()

ans = 0
inorder(3)             # 3을 루트노드로 했을 때, 최종 노드의 번호
print(ans)