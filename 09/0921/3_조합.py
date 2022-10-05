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


print()
# ------------------------------------------------------------------------

# 오름차순 조합
def nCr(s):
    if len(ans) == M:
        print(*ans)
    else:
        for i in range(s, N+1):
            if i not in ans:
                ans.append(i)
                nCr(i+1)
                ans.pop()

N, M = 4, 2
ans = []
nCr(1)