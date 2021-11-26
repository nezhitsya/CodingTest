def solution(s):
    answer = []
    
    s = s[2: -2]
    s = s.split("},{")
    s.sort(key = len)
    
    for i in s:
        i_split = i.split(",")
        for j in i_split:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer

# import re
# from collections import Counter

# def solution(s):

#     s = Counter(re.findall('\d+', s))
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse = True)]))