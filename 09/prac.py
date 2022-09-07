numbers = list(range(1, 10001))
rmnums = list()


for num in numbers:
    for i in str(num):
        num += int(i)
    rmnums.append(num)

ansnum = set(numbers) - set(rmnums)
for n in sorted(ansnum):
    print(n)
