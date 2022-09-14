import sys
from collections import defaultdict
sys.stdin = open('input.txt')

def node(k, lst):               # k : 노드 레벨 / lst :빌딩 트리 inorder 순환 배열
    global dic
    if k > 1:                   # 노드 레벨 1보다 클 때
        c = ((2**k)-1)//2       # 중앙 값 구하기 -> 노드 개수 // 2
        dic[k].append(lst[c])   # 딕셔너리 레벨값(리스트)에 중앙 값 삽입
        node(k-1, lst[:c])      # 레벨 하나 다운 / 왼쪽 리스트
        node(k-1, lst[c+1:])    # 레벨 하나 다운 / 오른쪽 리스트
    else:
        dic[k].append(lst[0])   # 노드 레벨 1일때 -> 자식 없음 -> 딕셔너리 레벨 밸류 값(리스트)에 삽입
                                # 어차피 리스트에 숫자 1개 있을 거라, lst[0]으로 표기

K = int(sys.stdin.readline())
build = list(map(int, sys.stdin.readline().split()))

dic = defaultdict(list)             # 리스트 값을 가지는 딕셔너리
node(K, build)                      # 함수 실행
# print(dic)

for ans in dic.values():
    print(*ans)