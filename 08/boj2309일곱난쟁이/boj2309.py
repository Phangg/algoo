import sys
sys.stdin = open('input.txt')

N = 9                                           # 입력 될 난쟁이들의 키는 9개
tall_lst = []
for _ in range(N):
    tall_lst.append(int(input()))               # 입력되는 난쟁이들의 키를 모두 리스트에 넣기

total = 0
for i in tall_lst:                              # 아홉 난쟁이들의 키의 합
    total += i

t = total - 100                                 # 일곱 난쟁이들의 키의 합은 100 / 그 차이를 이루는 난쟁이들을 찾기
fake_lst = []                                   # 일곱 난쟁이가 아닌, 두 난쟁이를 넣어줄 리스트
for j in range(N-1):
    for k in range(j+1, N):
        if tall_lst[j] + tall_lst[k] == t:      # 아홉 난쟁이들의 키 리스트 안에 두 난쟁이의 키의 합이 t 와 같다면 fake_lst 에 추가
            fake_lst.append(tall_lst[j])
            fake_lst.append(tall_lst[k])
            break
    if len(fake_lst) == 2:                      # 합이 같게 나오는 경우가 여러 경우일 때, 어떤 조합이든 상관 없지만, 여러개를 리스트에 추가하면 안됨
        break

ans_lst = [x for x in tall_lst if x not in fake_lst]    # tall_lst - fake_lst -> 차집합

# 삽입 정렬을 통한 정렬

for i in range(len(ans_lst)):
    while ans_lst[i-1] > ans_lst[i] and i > 0:
        ans_lst[i-1], ans_lst[i] = ans_lst[i], ans_lst[i-1]
        i -= 1

for ans in ans_lst:
    print(ans)