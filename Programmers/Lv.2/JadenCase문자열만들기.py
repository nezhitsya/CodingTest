def solution(s):
    answer = []
    arr = s.split(' ')
    
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    
    return ' '.join(arr)

# def solution(s):
#     return s.title()