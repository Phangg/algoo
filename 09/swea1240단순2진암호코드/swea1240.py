import sys
sys.stdin = open('input.txt')

# 숫자 값을 저장해 놓은 딕셔너리
num_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]       # 리스트에 한줄을 하나의 문자열로 입력 받음
    # print(arr)
    x = []
    for line in arr:
        if '1' in line:                     # 한 문자열에 '1'이 있는 줄만 x로 뽑아내기
            x = line
            break
    # print(x)
    e = 0
    for i in range(M-1, -1, -1):            # 뒤에서부터 탐색해서 1이 보이면 인덱스 저장하고 break
        if x[i] == '1':
            e = i
            break

    res = []
    s = (e - 56 + 1)
    for i in range(s, e, 7):                # 시작점을 -56 + 1 로 잡고 7개씩 체크
        res.append(num_dict[x[i:i+7]])      # 맨 위에 딕셔너리에서 값 변환 후, 리스트 추가
        # print(x[i:i+7])
    # print(res)

    even = odd = 0                          # even 짝수 / odd 홀수
    for idx, v in enumerate(res):
        if (idx+1) % 2:                     # 인덱스니까 idx + 1 해서 체크 / 홀수 짝수 값 만들기
            odd += v
        else:
            even += v
    code = even + (odd * 3)                 # 홀수 * 3  +  짝수
    # print(code)
    if code % 10:                           # 10의 배수가 아니면 0
        print(f'#{tc}', 0)
    else:                                   # 10의 배수이면, 전부 더한 값 출력
        print(f'#{tc}', even + odd)
