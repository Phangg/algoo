from bisect import bisect_left, bisect_right

# 단어들이 들어있는 arr 에 쿼리로 검색 가능한 개수 구하기
# ex) l: 'froaa', r: 'frozz' 로 해서 'fro??' 가 가능한 개수를 arr 에서 찾는 함수
def count_len(arr, l, r):
    r_idx = bisect_right(arr, r)
    l_idx = bisect_left(arr, l)
    return r_idx - l_idx


def solution(words, queries):
    answer = []
    for word in words:
        lst[len(word)].append(word)
        re_lst[len(word)].append(word[::-1])

    # 각 인덱스에 있는 리스트 정렬 (count_len 함수를 사용하기 위해 정렬 필요)
    for i in range(10001):
        lst[i].sort()
        re_lst[i].sort()

    for q in queries:
        # 뒤에 ? 가 오는 경우
        if q[0] != '?':
            res = count_len(lst[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        # 앞에서 부터 ? 가 오는 경우
        else:
            res = count_len(re_lst[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# 단어 길이를 인덱스로 가지도록, 단어를 저장할 2차원 리스트
lst = [[] for _ in range(10001)]
# 단어 길이를 인덱스로 가지도록, 단어를 뒤집어서 저장할 2차원 리스트
re_lst = [[] for _ in range(10001)]

print(solution(words, queries))
