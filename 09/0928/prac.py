# 인접 행렬 / 인접 리스트

# V :마지막 정점 번호(0부터 시작) / E : 간선 수
# 0 1 0 2 0 5 0 6 4 3 5 3 6 4 5 4

V, E = 6, 8
arr = list(map(int, input().split()))

# 인접 행렬
adj_m = [[0]*(V+1) for _ in range(V+1)]
# 인접 리스트
adj_lst = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adj_m[n1][n2] = 1
    adj_m[n2][n1] = 1                   # 무방향 일 때,

    adj_lst[n1].append(n2)
    adj_lst[n2].append(n1)

print(adj_m)
print(adj_lst)
