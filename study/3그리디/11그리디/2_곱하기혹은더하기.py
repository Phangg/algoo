import sys
sys.stdin = open('2input.txt')

s = list(map(int, sys.stdin.readline().rstrip()))
res = s[0]
for i in range(1, len(s)):
    res = max(res+s[i], res*s[i])
print(res)


# S = list(map(int, sys.stdin.readline().rstrip()))
# S.sort(reverse=True)
#
# ans = 1
# for s in S:
#     if s:
#         ans *= s
#     elif not s:
#         break
# print(ans)


# x = S[0]
# if x:
#     for i in range(1, len(S)):
#         if not S[i]:
#             x += S[i]
#         else:
#             x *= S[i]
# else:
#     for i in range(1, len(S)):
#         x += S[i]
#         if x:
#             for j in range(i+1, len(S)):
#                 if not S[j]:
#                     x += S[j]
#                 else:
#                     x *= S[j]
#             else:
#                 break
# print(x)