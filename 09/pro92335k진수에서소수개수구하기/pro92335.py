def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    change_num = ''
    m, d = 0, 0
    while n > k:
        m, d = divmod(n, k)
        change_num += str(d)
        n = m
        if m <= k:
            change_num += str(m)
    change_num = change_num[::-1]

    lst = change_num.split('0')
    answer = 0
    for n in lst:
        if n and is_prime(int(n)):
            answer += 1
    return answer