lst = []
def f(idx, n, r, res):
    if idx==r: 
        # print(res)
        lst.append(res[:])
        return
    for i in range(n):
        if i not in res: # if 분기가 없다면 중복
            res.append(i)
            f(idx + 1,n, r, res)
            res.pop()


N = 4
f(0, N, N-1, [])
print(lst)