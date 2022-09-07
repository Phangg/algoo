def f(i, r):
    # 멈추는 조건
    if i==r: 
        print(bit)
        return

    bit[i] = 0
    f(i+1,r)
    bit[i] = 1
    f(i+1,r)


N = 4
lst = list(range(1,N))
bit = [0]*N
f(0, N)