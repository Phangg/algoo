def f(i, r):
    if i==r: 
        print(bit[:r])
        return
    for n in range(N):
        if n not in bit[0:i]:
            bit[i] = n
            f(i+1,r)


N = 4
bit = [0]*N
f(0, N-1)