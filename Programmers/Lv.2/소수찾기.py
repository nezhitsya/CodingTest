import math
from itertools import permutations

def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def solution(numbers):
    answer = []
    
    for i in range(1, len(numbers) + 1):
        arr = list(permutations(numbers, i)) # 순열

        for j in range(len(arr)):
            num = int(''.join(map(str, arr[j])))
            if is_prime(num):
                answer.append(num)
    
    answer = list(set(answer)) # 중복제거
        
    return len(answer)

from itertools import permutations

# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)