from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    total = sum(queue1) + sum(queue2)
    goal = total // 2

    if total % 2:
        return -1

    round1 = 0
    a, b = sum(q1), sum(q2)
    while 1:
        if a == goal:
            break
        if a > goal:
            y = q1.popleft()
            q2.append(y)
            a -= y
            b += y
            round1 += 1
        else:
            x = q2.popleft()
            q1.append(x)
            a += x
            b -= x
            round1 += 1
        if round1 > (3 * len(queue1)):
            return -1

    q1 = deque(queue1)
    q2 = deque(queue2)
    a, b = sum(q1), sum(q2)
    round2 = 0
    while 1:
        if a == goal:
            break
        if b > goal:
            x = q2.popleft()
            q1.append(x)
            a += x
            b -= x
            round2 += 1
        else:
            y = q1.popleft()
            q2.append(y)
            a -= y
            b += y
            round2 += 1
        if round2 > (3 * len(queue1)):
            return -1

    if round1 > round2:
        answer = round1
    else:
        answer = round2

    return answer