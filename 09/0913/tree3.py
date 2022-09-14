def pre(n):
    if n <= size:
        print(tree[n])
        pre(2*n)
        pre(2*n + 1)


tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']        # 완전 이진 트리                  A
size = len(tree) - 1                            # 마지막 정점 번호             B      C
                                                #                          D   E  F
pre(1)
pre(2)