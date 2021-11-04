def solution(strings, n):
    answer = []
    
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()
    
    for j in range(len(strings)):
        answer.append(strings[j][1:])
    
    return answer

# def solution(strings, n):
#     '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
#     return sorted(strings, key=lambda x: x[n])