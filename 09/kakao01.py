from collections import defaultdict

terms_dict = defaultdict(int)
privacies_dict = defaultdict(list)


def terms_check(terms):
    global terms_dict
    char, num = '', ''
    for x in terms:
        char, num = x.split()
        num = int(num)
        terms_dict[char] = num


def privacies_check(privacies):
    global privacies_dict
    date, char = '', ''
    for i, x in enumerate(privacies):
        date, char = x.split()
        yyyy, mm, dd = date.split('.')
        date = [int(yyyy), int(mm), int(dd)]
        privacies_dict[i + 1] = [date, char]


def check(new_y, new_m, new_d, year, month, day):
    if new_y > year:
        return True
    elif new_y == year:
        if new_m > month:
            return True
        elif new_m == month:
            if new_d >= day:
                return True


def solution(today, terms, privacies):
    privacies_check(privacies)
    terms_check(terms)
    answer = []
    year, month, day = today.split('.')
    for i in range(len(privacies)):
        x = (terms_dict[privacies_dict[i + 1][1]] // 12)
        xx = (terms_dict[privacies_dict[i + 1][1]] % 12)

        tmp_m = privacies_dict[i + 1][0][1] + xx

        if tmp_m > 12:
            new_y = privacies_dict[i + 1][0][0] + x + (tmp_m // 12)
            new_m = tmp_m % 12
        else:
            new_y = privacies_dict[i + 1][0][0] + x
            new_m = tmp_m

        new_d = privacies_dict[i + 1][0][2] - 1
        if new_d == 0:
            if new_m > 1:
                new_m -= 1
            else:
                new_y -= 1
                new_m = 12
            new_d = 28

        res = check(new_y, new_m, new_d, int(year), int(month), int(day))

        if not res:
            answer.append(i + 1)

    return answer