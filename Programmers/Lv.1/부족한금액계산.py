def solution(price, money, count):
    answer = 0
    
    for i in range(1, count + 1):
        answer += price * i
    
    if money - answer < 0:
        answer = answer - money
    else:
        answer = 0

    return answer

# def solution(price, money, count):
#     return max(0, price * (count + 1) * count // 2 - money)