def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        result = []
        result = array[commands[i][0] - 1: commands[i][1]]
        result.sort()
        answer.append(result[commands[i][2] - 1])
    return answer

# def soultion(array, commands):
#     return list(map(lambda x: sorted(array[x[0] - 1: x[1]])[x[2] - 1], commands))