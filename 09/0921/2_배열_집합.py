# 배열의 합
def f(i, k):                # k : 원소 개수 / i : 선택된 원소의 수
    global min_v
    if i == k:
        s = 0               # a 행에서 p[a] 열을 골랐을 때의 합
        for a in range(k):
            s += arr[a][p[a]]
        if min_v > s:
            min_v = s
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

N = 3
arr = [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
p = [i for i in range(N)]
min_v = N * 10
f(0, N)
print(min_v)

# ------------------------------------------------------------------------

# 부분집합
arr = [3, 6, 7, 1, 5]
n = len(arr)

for i in range(0, 1 << n):              # 부분집합의 개수 (1부터 시작하면 공집합 x)
    for j in range(0, n):               # 원소 수만큼 비트 비교
        if i & (1 << j):                # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=' ')
    print()

print()

# 부분집합 2
arr = [1, 2, 3, 4, 5]
n = len(arr)

res = []
for i in range(1, 1 << n):
    tmp = []
    for j in range(0, n):
        if i & (1 << j):
            tmp.append(arr[j])
    res.append(tmp)
print(res)

print()

# 부분집합 3
A = [-1, 3, -9, 6, 7, -6, 1, 5, 4]
n = len(A)

ans = 0
for i in range(0, 1 << n):
    lst = []
    for j in range(0, n):
        if i & (1 << j):
            lst.append(A[j])
    if sum(lst) == 0:
        ans += 1
        print(lst)

# ------------------------------------------------------------------------

def f(i, k):
    if i == k:
        print(bit)
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)

arr = [3, 6, 7]
n = len(arr)
bit = [0] * n
f(0, n)

print()
# ------------------------------------------------------------------------

def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(arr[j], end=' ')
        print()
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 1
        f(i+1, k)

arr = [3, 6, 7]
n = len(arr)
bit = [0] * n
f(0, n)

print()