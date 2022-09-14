from collections import defaultdict


def solution(id_list, report, k):
    report = list(set(report))

    mail_dict = defaultdict(set)
    bad_dict = defaultdict(int)
    ban = []

    for mail in report:
        send, acc = mail.split(' ')
        mail_dict[send].add(acc)
        bad_dict[acc] += 1

    for bad in bad_dict:
        if bad_dict[bad] >= k:
            ban.append(bad)

    answer = []
    for m in id_list:
        cnt = 0
        for b in ban:
            if b in mail_dict[m]:
                cnt += 1
        answer.append(cnt)

    return answer