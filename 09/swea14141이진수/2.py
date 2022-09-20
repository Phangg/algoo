testNum = int(input())

for test in range(1, 1 + testNum):
    n, s = input().split()
    res = ''
    for i in s:
        a = int(i, 16)  # int(n진수 숫자,  n) 하면 10진수 값나옴
        b = format(a, 'b')  # format(10진수, 바꿀진수키값) 하면 해당 진수로 바뀜
        # 'b'는 2 'o'는 8 'x'는 16
        c = b.zfill(4)  # zfill(n)은 n보다 자릿수가 작으면 앞을 0으로 채운다.
        res += c
    print(f'#{test} {res}')