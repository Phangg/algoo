import sys
sys.stdin = open('input.txt')

def preorder(n):
    if n:
        pre.append(tree[n])
        preorder(L_ch[n])
        preorder(R_ch[n])

def inorder(n):
    if n:
        inorder(L_ch[n])
        inn.append(tree[n])
        inorder(R_ch[n])

def postorder(n):
    if n:
        postorder(L_ch[n])
        postorder(R_ch[n])
        post.append(tree[n])

N = int(sys.stdin.readline())
tree = [0] * (N+1)
L_ch = [0] * (N+1)
R_ch = [0] * (N+1)
pre, inn, post = [], [], []
for _ in range(N):
    n, l, r = map(ord, sys.stdin.readline().split())
    tree[n - 64] = n - 64
    if l >= 65:
        L_ch[n - 64] = l - 64
    if r >= 65:
        R_ch[n - 64] = r - 64

preorder(1)
inorder(1)
postorder(1)

for a in pre:
    print(chr(a+64), end='')
print()
for b in inn:
    print(chr(b+64), end='')
print()
for c in post:
    print(chr(c+64), end='')
print()