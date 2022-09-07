T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]
    res = 0
    s = n //2                            # 시작점과 끝점과 가운데점
    e = n //2
    c = n //2

    for i in range(n):
        for j in range(s, e+1):             # 가운데 한개부터 더하기 시작
            res += arr[i][j]
        if i < c:                           # 중간지점까지 한칸씩 커지다
            s -= 1
            e += 1
        else:                               # 그이후로 작아지면서 더해라
            s += 1
            e -= 1

    print(f'#{t} {res}')