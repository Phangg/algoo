import sys
sys.stdin = open('input.txt')

def bbg(lst):
    tri, rrr = 0, 0
    nums = [0 for _ in range(10 + 2)]
    for l in lst:
        nums[l] += 1
    for i, n in enumerate(nums):
        if n >= 3:
            nums[i] -= 3
            tri += 1
            continue
        if nums[i] >= 1 and nums[i+1] >= 1 and nums[i+2] >= 1:
            nums[i] -= 1
            nums[i + 1] -= 1
            nums[i + 2] -= 1
            rrr += 1
            continue
    if tri or rrr:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    A, B = [], []
    win = 0
    for idx, t in enumerate(card):
        if idx % 2:                     # 홀수 인덱스 => 플레이어 2 : B
            B.append(t)
            if len(B) >= 3:
                if bbg(B):
                    win = 2
                    break
        else:                           # 짝수 인덱스 => 플레이어 1 : A
            A.append(t)
            if len(A) >= 3:
                if bbg(A):
                    win = 1
                    break
    print(f'#{tc} {win}')