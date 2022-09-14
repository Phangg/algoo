from collections import defaultdict

def solution(survey, choices):
    ans_dic = defaultdict(int)
    for i in range(len(survey)):
        if choices[i] > 4:
            ans_dic[survey[i][1]] += (choices[i]-4)
        else:
            ans_dic[survey[i][0]] += (4-choices[i])

    answer = ''
    if ans_dic['R'] >= ans_dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if ans_dic['C'] >= ans_dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if ans_dic['J'] >= ans_dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if ans_dic['A'] >= ans_dic['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer