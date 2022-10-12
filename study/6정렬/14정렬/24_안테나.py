import sys
sys.stdin = open('24input.txt')

N = int(input())
h_lst = list(map(int, input().split()))
h_lst.sort(reverse=True)                    # 작은 값을 뽑을 거라서, 거꾸로 정렬
# print(h_lst)

ans_dic = dict()                            # 위치를 value로, 각 집과 떨어진 값의 합을 key로 가질 것
for i in range(N):
    ans = 0                                 # 내림차순 정렬이라, 같은 합을 가지는 경우 value 에 작은 값이 들어감
    for j in range(N):
        ans += abs(h_lst[i]-h_lst[j])
    ans_dic[ans] = h_lst[i]
# print(ans_dic)

print(ans_dic.get(min(ans_dic.keys())))     # 가장 작은 키값을 가지는 밸류를 출력