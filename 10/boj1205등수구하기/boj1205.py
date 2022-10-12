import sys
sys.stdin = open('input.txt')

N, T, P = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

# 주어진 리스트(N) >= 담을수 있는 리스트 공간(P)
# 리스트 마지막 숫자보다 태수 숫자가 작거나 같을 때
if N >= P and T <= num[-1]:
    print(-1)
    exit()

# 주어진 리스트가 P와 같거나 더 작을 때
elif N <= P:
    if T in num:                # 이미 있는 숫자라면 그 숫자 인덱스 + 1 => 0번 인덱스가 1번째라서
        print(num.index(T)+1)
    else:
        num.append(T)           # 없는 숫자면 append / 다시 내림차순 정렬 후 출력
        num.sort(reverse=True)  # 내 숫자가 뒤로 더 밀릴 경우는 없다 => 이 경우는 맨위에 if 문에서 걸렀으니깐
        print(num.index(T)+1)