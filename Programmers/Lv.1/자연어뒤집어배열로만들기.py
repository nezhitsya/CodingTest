def solution(n):
    answer = []
    
    for i in range(len(str(n)) - 1, -1, -1):
        n_list = str(n)
        answer.append(int(n_list[i]))
        
    return answer

# def solution(n):
#     return list(map(int, reversed(str(n))))

# def solution(n):
#     return [int(i) for i in str(n)][::-1]
