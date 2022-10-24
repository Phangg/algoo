# 현재 res (만들어진 기둥과 보의 상태)가 가능한지 체크
def check(res):
    for tmp in res:
        x, y, what = tmp
        # 보
        if what:
            # 왼쪽에 기둥        or      오른쪽에 기둥         or      왼편에 보 + 오른편에도 보
            if ([x, y - 1, 0] in res) or ([x + 1, y - 1, 0] in res) or ([x - 1, y, 1] in res and [x + 1, y, 1] in res):
                pass
            else:
                return 0
        # 기둥
        elif not what:
            # 현재 바닥     or  바로 밑에 기둥    or      보가 끝나는 지점     or  보가 시작 되는 지점
            if (y == 0) or ([x, y - 1, 0] in res) or ([x - 1, y, 1] in res) or ([x, y, 1] in res):
                pass
            else:
                return 0
    return 1


def solution(n, build_frame):
    res = []
    for info in build_frame:
        x, y, what, how = info
        # 설치
        if how:
            res.append([x, y, what])
            # 만들면 안된다 -> NO 설치
            if not check(res):
                res.remove([x, y, what])
        # 삭제
        elif not how:
            res.remove([x, y, what])
            # 삭제하면 안된다 -> 다시 append
            if not check(res):
                res.append([x, y, what])
    return sorted(res)


n = 5

# build_frame = [
#     [1, 0, 0, 1],
#     [1, 1, 1, 1],
#     [2, 1, 0, 1],
#     [2, 2, 1, 1],
#     [5, 0, 0, 1],
#     [5, 1, 0, 1],
#     [4, 2, 1, 1],
#     [3, 2, 1, 1]
# ]

build_frame = [
    [0, 0, 0, 1],
    [2, 0, 0, 1],
    [4, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [2, 1, 1, 1],
    [3, 1, 1, 1],
    [2, 0, 0, 0],
    [1, 1, 1, 0],
    [2, 2, 0, 1]
]

print(solution(n, build_frame))

# result
# [[1, 0, 0], [1, 1, 1], [2, 1, 0], [2, 2, 1], [3, 2, 1], [4, 2, 1], [5, 0, 0], [5, 1, 0]]

# result
# [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]
