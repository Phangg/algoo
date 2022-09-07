# 부분 집합

def f(i, N):
    if i == N:
        print(bit)
    else:
        bit[i] = 1          # A[i]가 부분집합에 포함
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1, 2, 3]
bit = [0] * 3
f(0, 3)


print()
#-----------------------------------------------------------------

def f(i, N):
    if i == N:
        for i in range(N):
            if bit[i]:
                print(A[i], end=' ')
        print()
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1, 2, 3]
bit = [0] * 3
f(0, 3)


print()
#-----------------------------------------------------------------

def f(i, N):
    global ans
    global cnt
    cnt += 1
    if i == N:
        s = 0                       # 부분 집합의 합
        for i in range(N):
            if bit[i]:
                s += A[i]
        if s == 10:
            ans += 1                # 부분집합의 합이 10 인 경우의 수
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
ans = 0
cnt = 0
f(0, 10)
print(ans, cnt)


print()
#-----------------------------------------------------------------

def f(i, N):
    global ans
    if i == N:
        s = 0                       # 부분 집합의 합
        for i in range(N):
            if bit[i]:
                s += A[i]
        if s == 10:
            ans += 1                # 부분집합의 합이 10 인 경우의 수
            for i in range(N):
                if bit[i]:
                    print(A[i], end=' ')
            print()
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
ans = 0
f(0, 10)


print()
#-----------------------------------------------------------------

# 부분 집합 2

def f(i, N, s, t):
    global ans
    global cnt
    cnt += 1
    if i == N:                      # 모든 원소가 고려된 경우
        if s == t:                  # 부분 집합의 합이 t이면
            ans += 1
        return
    elif s > t:
        return
    else:
        f(i+1, N, s+A[i], t)        # A[i]가 포함 된 경우
        f(i+1, N, s, t)             # A[i]가 포함되지 않은 경우

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
ans = 0
cnt = 0
f(0, 10, 0, 10)
print(ans, cnt)


print()
#-----------------------------------------------------------------

# 순열

def f(i, N):
    if i == N:
        print(p)
    else:
        for j in range(i, N):       # p[i]에 들어갈 숫자 p[j] 결정
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i]

p = [1, 2, 3]
f(0, 3)