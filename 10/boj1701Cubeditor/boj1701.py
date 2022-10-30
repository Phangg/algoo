import sys
sys.stdin = open('input.txt')

# x: 패턴
def failure(x):
    table = [0] * len(x)                # 반복가능한 길이 체크를 위한 테이블 생성
    j = 0                               # 문자열 길이 체크 / 패턴 체크 위한 j
    for i in range(1, len(x)):          # j가 0부터, i가 1번 부터 뒤로 하나씩 가면서 비교
        while j > 0 and x[i] != x[j]:
            j = table[j-1]
        if x[i] == x[j]:                # 둘이 같으면, 중복되는게 시작 되었다는..
            j += 1
            table[i] = j
    return table

S = sys.stdin.readline().rstrip()

# 전체 배열?을 하나씩 앞에서 줄여가면서  함수 값과 ans 의 max 체크
ans = 0
for i in range(len(S)):
    ans = max(ans, max(failure(S[i:])))
print(ans)

# https://peisea0830.tistory.com/65 참고했음..
# KMP 보다보니, failure 배열에 대한 이해를 하고 풀어야한다더라.
