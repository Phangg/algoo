import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    ans = []
    num = 666
    while len(ans) < 10001:
        if '666' in str(num):
            ans.append(num)
        num += 1
    print(ans[n-1])