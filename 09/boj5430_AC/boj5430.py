import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    lst = sys.stdin.readline()[1:-2].split(',')
    # print(lst)

    q = deque()
    for i in lst:
        if i.isdigit():
            q.append(int(i))
    # print(q)

    error = 0
    r_flag = 0
    for j in p:
        if j == 'D':
            if q:
                if not r_flag:
                    q.popleft()
                else:
                    q.pop()
            else:
                error = 1
                break
        else:
            r_flag = (r_flag+1) % 2

    ans = []
    if error:
        print('error')
    else:
        if r_flag:
            while q:
                ans.append(q.pop())
        else:
            while q:
                ans.append(q.popleft())
        ans = '[' + ','.join(map(str, ans)) + ']'
        print(ans)