def solution(nums):
    answer = len(set(nums))
    
    if len(nums) / 2 > answer:
        return answer
    else:
        return len(nums) / 2

# def solution(ls):
#     return min(len(ls)/2, len(set(ls)))
