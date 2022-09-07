# atoi -> 문자열을 숫자로
# itoa -> 숫자를 문자열로
# (단, 자연수 -> 정수)

from operator import le
from re import I


def atoi(x: str):
    i = 0
    for a in x:
        i = i * 10
        i += ord(a) - ord('0')  # 아스키지만 숫자값에서 '0' 아스키 값을 빼면 int 값이다..
    return i


def itoa(i: int):
    if i == 0:
        return '0'

    is_positive = True
    if i < 0:
        is_positive = False
        i = -i

    ans = ''
    while i:
        i, d = divmod(i, 10)   # i, d = i // 10, i % 10
        ans = chr(d + ord('0')) + ans
    
    if is_positive:
        return ans 
    else:
        return '-' + ans

if __name__ == "__main__":
    print(atoi('A'))
    print(itoa(10))

# --------------------------------------------------------------------

# 브루트포스 1 

def func(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
            else:
                return i
        return -1

# --------------------------------------------------------------------

# 브루트포스 2

def func(text, pattern):
    m = len(pattern)
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + m] == pattern:
            return i
    return -1

# --------------------------------------------------------------------

