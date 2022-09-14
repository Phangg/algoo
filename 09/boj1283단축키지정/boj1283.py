import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
danchuk = []
for _ in range(N):
    word = list(map(str, sys.stdin.readline().split()))
    # print(word)

    for i in range(len(word)):                                  # 단어들의 첫글자 먼저 체크
        if word[i][0].lower() not in danchuk:
            danchuk.append(word[i][0].lower())
            word[i] = '[' + word[i][0] + ']' + word[i][1:]
            print(' '.join(word))
            break
    else:
        for j in range(len(word)):                              # 각 단어의 첫글자가 이미 단축키 일 떄
            tmp = 0                                             # 브레이크 용 변수
            for k in range(1, len(word[j])):                    # 첫 단어의 두번째 글자부터 탐색
                if word[j][k].lower() not in danchuk:
                    danchuk.append(word[j][k].lower())
                    tmp = 1
                    word[j] = word[j][:k] + '[' + word[j][k] + ']' + word[j][k+1:]
                    print(' '.join(word))
                    break
            if tmp == 1:
                break
        else:                                                   # 위에 모든 걸 다 돌았는데, print / break 되지 않은 경우
            print(*word)                                        # 그냥 단어 그대로 출력