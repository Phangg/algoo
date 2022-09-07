import sys
sys.stdin = open('input.txt')

# w: 가로 / h: 세로 / p,q: 초기 위치 좌표 / t: 시간
w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

x = (p + t) // w            # 짝수 -> 증가 / 홀수 -> 감소
y = (q + t) // h

if x % 2:
    print(w - ((p + t) % w), end=' ')
else:
    print((p + t) % w, end=' ')

if y % 2:
    print(h - ((q + t) % h), end=' ')
else:
    print((q + t) % h, end=' ')