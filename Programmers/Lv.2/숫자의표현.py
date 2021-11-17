def solution(n):
    answer = 0

    for i in range(1, n + 1):
        sum_num = 0
        for j in range(i, n + 1):
            sum_num += j
            if sum_num == n:
                answer += 1
                break
            elif sum_num > n:
                break
    
    return answer

def solution(num):
    return len([i  for i in range(1, num + 1, 2) if num % i is 0])