def solution(lottos, win_nums):
    answer = [7, 7]
    for i in range(len(win_nums)):
        if win_nums[i] in lottos:
            answer[0] -= 1
            answer[1] -= 1
        if lottos[i] == 0:
            answer[0] -= 1
    if answer[0] == 7:
        answer[0] = 6
    if answer[1] == 7:
        answer[1] = 6

    return answer

# def solution(lottos, win_nums):
#     rank=[6,6,5,4,3,2,1]
#     cnt_0 = lottos.count(0)
#     ans = 0
#
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]
