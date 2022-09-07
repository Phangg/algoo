import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
x = 0
ans = []                        # 숫자가 가장 많을 때, 리스트
max_cnt = 0                     # 숫자 개수
for i in range(N//2, N+1):      # i 는 두번째 숫자 (주어지는 숫자의 반부터 시작 , 주어진 숫자도 포함)
    lst = []                    # 반복을 돌려 줄 리스트 / 돌때 마다 초기화
    lst.append(N)               # N 주어진 첫 숫자
    lst.append(i)               # for문에서 순회 중인 두번째 숫자
    x = N - i
    cnt = 2                     # 리스트에 있는 숫자 개수 (밑에 while문 종료 시, 재시작 전 초기화)
    n = N                       # N을 while 문에서 사용하기 위해 n 에 값 복사
    while x >= 0:               # x가 음수일 때 까지
        lst.append(x)           # x는 N-i
        cnt += 1                # x 삽입 시, +1
        n = i                   # n, i 자리 이동
        i = x
        x = n - i               # x 생성 / 음수이면 종료 됨
        if max_cnt < cnt:       # while 재시작 이전에, cnt 초기화되니까 -> max_cnt 체크
            max_cnt = cnt
            ans = lst[:]        # max_cnt 일때, 현재 리스트 외부 ans 리스트에 저장
print(max_cnt)
print(*ans)
