# 삽입 정렬

lst = [4, 8, 1, 5, 7]

for i in range(1, len(lst)):
    while lst[i - 1] > lst[i] and i > 0:
        lst[i - 1], lst[i] = lst[i], lst[i - 1]
        i -= 1
print(lst)


#     for j in range(i, 0, -1):
#         if lst[j-1] > lst[j]:
#             lst[j-1], lst[j] = lst[j], lst[j-1]
# print(lst)
