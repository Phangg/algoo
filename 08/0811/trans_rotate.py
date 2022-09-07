lst = [[1,2,3],[4,5,6],[7,8,9]]

for i in lst:
    print(*i)
print()

lst1 = list(map(list,zip(*lst)))
for i in lst1:
    print(*i)
print()

lst2 = list(zip(*lst))[::-1]
for i in lst2:
    print(*i)
print()

lst3 = list(zip(*lst[::-1]))
for i in lst3:
    print(*i)
print()
