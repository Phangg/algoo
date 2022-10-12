'''
3 3
1 2
1 3
2 3
'''

def find_P(parent, x):
    if parent[x] != x:
        parent[x] = find_P(parent, parent[x])
    return parent[x]


def union_P(parent, a, b):
    a = find_P(parent, a)
    b = find_P(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [k for k in range(0, v+1)]

cycle = False
for i in range(e):
    a, b = map(int, input().split())
    if find_P(parent, a) == find_P(parent, b):
        cycle = True
        break
    else:
        union_P(parent, a, b)

if cycle:
    print('OUI')
else:
    print('NON')