import sys
sys.stdin = open('input_babygin.txt')

def f(i, k):
    global ans
    if i == k:
        run = 0
        tri = 0
        if card[0] == card[1] and card[1] == card[2]:
            tri += 1
        if card[0] + 1 == card[1] and  card[1] + 1 == card[2]:
            run += 1
        if card[3] == card[4] and card[4] == card[5]:
            tri += 1
        if card[3] + 1 == card[4] and  card[4] + 1 == card[5]:
            run += 1
        if tri + run == 2:
            ans = 'BabyGin'
    else:
        for j in range(i, k):
            card[i], card[j] = card[j], card[i]
            f(i+1, k)
            card[i], card[j] = card[j], card[i]


T = int(input())
for _ in range(T):
    card = list(map(int, input()))
    ans = 'Lose'
    f(0, 6)
    print(ans)