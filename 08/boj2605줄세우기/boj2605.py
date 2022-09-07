import sys
sys.stdin = open('input.txt')

# 0 제자리 / 뽑은 번호만큼 앞으로 감
S = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

ans = []
lst = []
for idx, n in enumerate(nums, 1):
    lst.append([idx, n])
# print(lst)

for i in range(S):
    ans.insert(len(ans)-lst[i][1], lst[i][0])       # insert(i, x) -> i 인덱스 앞에 x 넣기
print(*ans)