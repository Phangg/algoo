import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    lst = [[''] * 10 for _ in range(10)]  # 비어있는 문자열로 10*10 체크 / 이후에 중복 되지 않게 하기 편하려고
    N = int(input())
    for _ in range(N):
        arr = list(map(int, input().split()))

        if arr[-1] == 1:  # 리스트 마지막에 컬러 색상 확인
            for i in range(arr[0], arr[2]+1):  # 예시로 보면 2,2 부터 4,4 까지 색칠 하니까
                for j in range(arr[1], arr[3]+1):  # 리스트에 입력 된 순서는 포인트 위치랑 변동 없으니, 인덱스 직접 입력
                    if 'r' not in lst[i][j]:  # 'r' 가 이미 있으면 중복 칠하지 말아라
                        lst[i][j] += 'r'

        elif arr[-1] == 2:
            for i in range(arr[0], arr[2]+1):
                for j in range(arr[1], arr[3]+1):
                    if 'b' not in lst[i][j]:
                        lst[i][j] += 'b'

        cnt = 0
        for i in range(10):
            for j in range(10):
                if 'r' in lst[i][j] and 'b' in lst[i][j]:
                    cnt += 1
    print(f'#{tc} {cnt}')





