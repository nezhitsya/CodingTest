def isPrime(a, b, c):
    total = a + b + c

    for i in range(2, total): 
        if total % i == 0 : return False 
    return True 

def solution(nums):
    answer = 0

    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if isPrime(nums[i], nums[j], nums[k]): answer += 1

    return answer

# from itertools import combinations as cb

# def solution(nums):
#     answer = 0
#     for a in cb(nums, 3):
#         cand = sum(a)
#         for j in range(2, cand):
#             if cand % j == 0:
#                 break
#         else:
#             answer += 1
#     return answer