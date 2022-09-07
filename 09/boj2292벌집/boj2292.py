import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

num = 1             # 반복의 첫 숫자
ans = 0             # 몇번째 굴레?
while 1:
    num += (6*ans)  # 1, 2, 8, 20 ... (6의 배수를 더해줌)
    ans += 1        # 한 칸씩 나아감
    if num >= N:    # 제시된 숫자가 더 작다면 멈추기
        break
print(ans)