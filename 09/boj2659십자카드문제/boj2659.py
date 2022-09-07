import sys
sys.stdin = open('input.txt')

def minN(n):                                            # 숫자 4개를 가지고, 시게 방향으로 돌려서 가질 수 있는 최소 값을 구하는 함수
    min_num = n                                         # 시작 값을 최소 값으로 설정 후,
    for _ in range(3):
        n = (n % 1000) * 10 + (n // 1000)               # 일,십,백 자리 수를 하나씩 올리고 1000으로 나눠진 몫을 일의 자리로 변경
        if min_num > n:
            min_num = n                                 # 최소 값 체크
    return min_num

num = int(''.join(sys.stdin.readline().split()))        # join을 통해 처음부터 2112의 int형태로 받아주기
ans_num = minN(num)

x = 1111
cnt = 0
while x <= ans_num:
    if minN(x) == x:                                    # 예시에서 1112 와 1121 은 겹쳐서 하나만 생각한다고 했으니, 함수 돌려서 판단
        cnt += 1
    x += 1

print(cnt)
