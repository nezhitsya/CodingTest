def solution(s):
    s_split = s.split(' ')
    answer = []
    
    for ss in s_split:
        s_list = list(ss)
        
        for i in range(len(s_list)):
            if i % 2 == 0:
                s_list[i] = s_list[i].upper()
            else:
                s_list[i] = s_list[i].lower()
        answer.append(''.join(s_list))
    
    return ' '.join(answer)

# def solution(s):
#     return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))