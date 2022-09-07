import sys
sys.stdin = open('input.txt')

N, M = list(map(int, sys.stdin.readline().split()))

all_num_lst = []
num_lst = []
for _ in range(M):
    k = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    num_lst.append(nums)                                 # 책 더미를 하나의 리스트로 가지는 2차원 리스트
    all_num_lst += nums                                  # 모든 책을 담고 있는 리스트 생성

stack = []                                               # 스택 생성
ans = 0
while len(all_num_lst) > 0:                              # all 리스트 가 비어있지 않은 동안
    for x in range(M):
        if len(num_lst[x]) > 0:                          # 책 더미에 책이 남아있다면
            if min(all_num_lst) != num_lst[x][-1]:       # 책 더미 맨위에 있는 책이 모든 책들 중 제일 작은 번호가 아닐때
                ans = 0                                  # ans = 0 -> false 를 가리키고 / break
                break
            else:
                stack.append(num_lst[x][-1])             # 책 더미 맨위에 모든 책에서 가장 작은 넘버의 책이 있다면
                num_lst[x].pop(-1)                       # 더미에서 뽑아주기
                all_num_lst.remove(min(all_num_lst))     # 뿐만 아니라, 모든 책 리스트에서도 제거
                ans = 1                                  # ans = 1 -> true
if ans == 1:
    print('Yes')
 else:
    print('No')

실패...
---------------------------------------------------
# 방법을 바꿔서 처음에 생각했다가 안될 것 같은데? 했던 방식으로..
# 각 더미에서 정렬이 안되어있다면 애초에 불가능하지 않나?
# 예외가 있으려나? + sort 혹은 [::-1] 안쓰고 싶기도 해서 안했지만, 이게 답이었다.

N, M = list(map(int, sys.stdin.readline().split()))

ans = 1                                                   # true 를 기본으로 두고 진행
for _ in range(M):
    k = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))   # 1차원 배열
    if nums != sorted(nums, reverse=True):                # nums 는 애초에 내림차순으로 리스트 입력이라, reverse+True (내림차순)으로 sort한 것과 다르다면 ans = 0 -> false / break
        ans = 0
        break

if ans == 1:
    print('Yes')
else:
    print('No')