'''
6 4
1 4
2 3
2 4
5 6
'''

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트노드 일 때까지 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 있는 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 두 원소 중 작은 원소를 루트로 하자
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# v: 노드의 개수 / e: 간선의 개수
v, e = map(int, input().split())
# 부모 테이블
parent = [0] * (v+1)

# 부모 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

# union 함수 GO!
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 (각 원소의 루트노드) 출력
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력
for i in range(1, v+1):
    print(parent[i], end=' ')
print()