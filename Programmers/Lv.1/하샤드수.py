def solution(x):
    x_list = list(str(x))
    answer = 0
    
    for i in range(len(x_list)):
        answer += int(x_list[i])
        
    if x % answer == 0 or answer % x == 0:
        return True
    else:
        return False

# def solution(n):
#     return n % sum([int(c) for c in str(n)]) == 0