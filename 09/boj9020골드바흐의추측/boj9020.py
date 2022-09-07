import sys
sys.stdin = open('input.txt')

def is_prime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if x % i == 0:
            return False
    return True

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())

    # 가운데서부터 가니까 가장 차이가 작은 값 추출 가능
    for num in range(n//2, -1, -1):
        if is_prime(num) and is_prime(n - num):
            print(num, n-num)
            break