text = 'this is book'
pattern = 'is'
# pattern in text
def func(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
        else:
            return i
    return -1

def func2(text, pattern):
    m = len(pattern)
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+m] == pattern:
            return i
    return -1

# def func3(text, pattern):
#     i = 0
#     j = 0
#     while i<len(text) and j<len(pattern):
#         if text[i] != pattern[j]:
#             i = i-j
#             j = -1
#         i = i+1
#         j = j+1
#     if j== len(pattern):
#         return i-len(pattern)
#     else:
#         return -1

if __name__ == '__main__':
    text = 'this is book'
    pattern = 'is'
    print(func(text, pattern))




