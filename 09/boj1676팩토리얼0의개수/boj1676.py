import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

NP = 1
for i in range(N, 0, -1):
    NP *= i

NP = str(NP)
ans = 0
for i in range(len(NP)-1, -1, -1):
    if NP[i] == '0':
        ans += 1
    else:
        break
print(ans)