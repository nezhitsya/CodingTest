def solution(sizes):
    answer = 0
    max_x = 0
    max_y = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
        
        max_x = max(sizes[i][0], max_x)
        max_y = max(sizes[i][1], max_y)
    
    answer = max_x * max_y
    
    return answer

# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)