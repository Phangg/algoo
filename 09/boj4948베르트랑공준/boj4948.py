import sys
sys.stdin = open('input.txt')

def is_prime(num):
    for i in range(2, int((2 * n) ** 0.5) + 1):
        if num % i == 0:
            prime_dic[num] = 0      # 메모이제이션
            return 0
    prime_dic[num] = 1
    return 1

prime_dic = {}                      # 메모이제이션

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    ans = 0
    for num in range(n+1, (2*n)+1):
        if num in prime_dic.keys():
            ans += prime_dic[num]   # 가지고 있는 값인가?
        else:
            ans += is_prime(num)
    print(ans)