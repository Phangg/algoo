import sys
sys.stdin = open('input.txt')

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    order = sys.stdin.readline().rstrip()
    if ' ' in order:
        og, n = order.split()
        n = int(n)
        if og == 'add':
            S.add(n)
        elif og == 'remove':
            if n in S:
                S.remove(n)
        elif og == 'check':
            if n in S:
                print(1)
            else:
                print(0)
        elif og == 'toggle':
            if n in S:
                S.remove(n)
            else:
                S.add(n)
    elif order == 'all':
        S = set(range(1, 21))
    elif order == 'empty':
        S.clear()
