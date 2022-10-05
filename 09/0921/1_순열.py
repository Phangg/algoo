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
# ---------------

# 재귀 호출을 통한 순열 생성 2
def f(x, y):
    global res
    if x == y:
        res.append(p[:])
    else:
        for i in range(x, y):
            p[x], p[i] = p[i], p[x]
            f(x+1, y)
            p[x], p[i] = p[i], p[x]

p = [1, 2, 3, 4]
res = []
f(0, 4)
print(res)

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

