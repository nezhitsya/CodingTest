def solution(answers):
    answer = []
    student = [0, 0, 0]
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == s1[i % len(s1)]:
            student[0] += 1
        if answers[i] == s2[i % len(s2)]:
            student[1] += 1
        if answers[i] == s3[i % len(s3)]:
            student[2] += 1

    for i in range(len(student)):
        if student[i] == max(student):
            answer.append(i + 1)

    return answer

# def solution(answers):
#     p = [[1, 2, 3, 4, 5],
#          [2, 1, 2, 3, 2, 4, 2, 5],
#          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
#     s = [0] * len(p)

#     for q, a in enumerate(answers):
#         for i, v in enumerate(p):
#             if a == v[q % len(v)]:
#                 s[i] += 1
#     return [i + 1 for i, v in enumerate(s) if v == max(s)]