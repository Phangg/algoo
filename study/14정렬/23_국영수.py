import sys
from pprint import pprint

sys.stdin = open('23input.txt')

N = int(input())
s_lst = [[] for _ in range(N)]
for n in range(N):
    name, ko, en, ma = input().split()      # 이름은 str으로, 점수는 int로 리스트에 넣어주기
    s_lst[n].append(name)
    s_lst[n].append(int(ko))
    s_lst[n].append(int(en))
    s_lst[n].append(int(ma))
# print(s_lst)

s_lst.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
pprint(s_lst)                               # sort 와 람다를 이용해서 정렬
                                            # '-'를 붙이면 역순으로 정렬 / ()안에 넣은 순서대로 우선 정렬

for student in s_lst:                       # 이름만 출력
    print(student[0])