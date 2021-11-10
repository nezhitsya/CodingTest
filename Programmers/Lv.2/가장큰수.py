def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key = lambda x : x * 3, reverse = True)
    return str(int(''.join(answer)))

# def solution(numbers):
#     answer = ''
#     numbers = sorted(numbers, reverse = True, key = lambda  x: (str(x) * 4).ljust(4))
#     for i in numbers:
#         answer += str(i)
#     if answer[0] == '0':    #모두 0인 경우 -> 테스트11
#         return '0'
#     return answer