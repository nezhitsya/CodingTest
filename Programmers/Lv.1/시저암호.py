def solution(s, n):
    answer = []
    
    for i in s:
        if i.isupper():
            answer.append(chr((ord(i) - ord('A') + n) % 26 + ord('A')))
        elif i.islower():
            answer.append(chr((ord(i) - ord('a') + n) % 26 + ord('a')))
        else:
            answer.append(' ')
    
    return ''.join(answer)

# def solution(s, n):
#     s = list(s)

#     for i in range(len(s)):
#         if s[i].isupper():
#             s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
#         elif s[i].islower():
#             s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

#     return ''.join(s)