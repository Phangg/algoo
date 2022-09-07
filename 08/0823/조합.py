def func(idx, n, r, res):
    if idx == r:
        print(res)
        return

    start = 0
    if res:
        start = max(res) + 1
        # start = max(res)  # +1이 없다면 중복 허용

    for i in range(start, n):

        res.append(i)
        func(idx+1, n, r, res)
        res.pop()

        # func(idx+1, n, r , res + [i])
        

func(0, 7, 3, [])