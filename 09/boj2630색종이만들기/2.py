import sys
sys.stdin = open('input.txt')


def paper(x, y, n):
    t = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if t != arr[i][j]:
                k = n // 2
                paper(x, y, k)
                paper(x, y + k, k)
                paper(x + k, y, k)
                paper(x + k, y + k, k)
                return

    color[t] += 1


n = int(sys.stdin.readline())
arr = []
color = [0, 0]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

paper(0, 0, n)

for i in range(2):
    print(color[i])