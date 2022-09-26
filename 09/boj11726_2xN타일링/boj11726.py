import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
ans = [0, 1, 2]
for a in range(3, 1001):
    ans.append(ans[a-1] + ans[a-2])
print(ans[n] % 10007)