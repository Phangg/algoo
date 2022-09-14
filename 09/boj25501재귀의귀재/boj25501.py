import sys
sys.stdin = open('input.txt')

def recursion(lst, s, e):
    global cnt
    cnt += 1
    if s >= e:
        return 1, cnt
    elif lst[s] != lst[e]:
        return 0, cnt
    else:
        return recursion(lst, s+1, e-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(sys.stdin.readline())
for _ in range(T):
    S = list(map(str, sys.stdin.readline().rstrip()))
    # print(S)
    cnt = 0
    print(*isPalindrome(S))
