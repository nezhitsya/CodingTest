def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        remv = min(arr)
        arr.remove(remv)
        return arr

# def solution(arr):
#     return [i for i in arr if i > min(arr)]