import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())
    clst = []                                       # Ci 와 Ki 를 각각 담을 리스트
    klst = []
    for _ in range(N):
        Ci, Ki = input().split()
        clst.append(Ci)
        klst.append(int(Ki))                        # Ki는 int 로 변환해서 담아주기
    res = ''
    for i in range(N):
        res += clst[i] * klst[i]                    # res 에 전부 이어진 문자열로 저장

    num = 0
    for j in res:
        print(j, end='')
        num += 1                                    # num 변수 설정으로 10글자 범위 체크하면서, 한글자씩 이어서 출력
        if num == 10:
            num = 0
            print()                                 # 줄 바꿈
    print()