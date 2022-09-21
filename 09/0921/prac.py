# 반복을 이용한 선택정렬
def selection_sort(a):
    n = len(a)

    for i in range(0, n-1):
        min_i = i
        for j in range(i+1, n):
            if a[j] < a[min_i]:
                min_i = j
        a[min_i], a[i] = a[i], a[min_i]

# ------------------------------------------------------------------------

# n!
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

# ------------------------------------------------------------------------

# {1,2,3} 을 포함하는 모든 순열을 생성
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            for k in range(1, 4):
                if k != i and k != j:
                    print(i, j, k)

print()
# ------------------------------------------------------------------------

# 재귀 호출을 통한 순열 생성
def f(i, k):                # k : 원소 개수 / i : 선택된 원소의 수
    if i == k:              # i == 원소 개수 => 출력
        print(p)
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3, 4]
f(0, 4)

print()
# ------------------------------------------------------------------------

# 재귀 호출을 통한 순열 생성 - 사전순으로 정의
# N 개 중에 R 개를 고르는 순열
def f(i, k, r):                     # k : 원소 개수 / i : 선택된 원소의 수 / r : 원하는 원소 개수
    if i == r:
        print(p)
    else:
        for j in range(k):
            if used[j] == 0:        # a[j]가 아직 사용되지 않았으면
                used[j] = 1         # a[j] 사용 표시
                p[i] = a[j]         # p[i] = a[j]
                f(i+1, k, r)        # p[i+1] 을 결정하러 이동
                used[j] = 0         # a[j]를 다른 자리에서 쓸 수 있도록 해제

N = 5
R = 3
a = [i for i in range(1, N+1)]
used = [0] * N
p = [0] * R
f(0, N, R)

print()
# ------------------------------------------------------------------------

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
# ------------------------------------------------------------------------

# 조합
N = 5
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            print(i, j, k)

print()
# ------------------------------------------------------------------------

# 조합
def nCr(n, r, s):
    if r == 0:
        print(*comb)
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]
            nCr(n, r-1, i+1)

A = [x for x in range(5)]
n = len(A)
r = 3
comb = [0] * r
nCr(n, r, 0)