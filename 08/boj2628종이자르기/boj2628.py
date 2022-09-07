import sys
sys.stdin = open('input.txt')

# w : 가로 / h : 세로
# L : 자르려는 선의 개수
w, h = map(int, sys.stdin.readline().split())
L = int(sys.stdin.readline())
point_lst = []
w_lst = []                                                  # 가로를 자르기 위한 포인터 리스트
h_lst = []                                                  # 세로를 자르기 위한 포인터 리스트
for _ in range(L):
    way, point = map(int, sys.stdin.readline().split())
    if way:
        w_lst.append(point)
    else:
        h_lst.append(point)
h_lst = sorted(h_lst, reverse=True)                         # 큰 숫자부터 작은 숫자로 내림차순 정렬
h_lst.append(0)                                             # 두 리스트 모두 정렬 후 , 0 삽입 (밑에서 설명)
w_lst = sorted(w_lst, reverse=True)
w_lst.append(0)

h_res = []
x = h                                                       # 자르기 전
for i in h_lst:                                             # 10에서 가장 큰 수를 빼고 남은 수를 결과 리스트에 삽입
    h_res.append(x - i)                                     # x 를 방금 뺏던 숫자로 바꿔서 반복
    x = i                                                   # 맨 마지막에 숫자를 빼기 위해, 위에서 리스트 마지막에 0 삽입
# print(h_res)

w_res = []
x = w
for i in w_lst:
    w_res.append(x - i)
    x = i
# print(w_res)

print(max(h_res) * max(w_res))