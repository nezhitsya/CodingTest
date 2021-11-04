def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        temp = bin(arr1[i] | arr2[i]) # 10진수 수를 2진수로
        temp = temp[2:].zfill(n) # 문자열 앞에 0 채우기
        temp = temp.replace('1', '#').replace('0', ' ')
        answer.append(temp)
    
    return answer

# def solution(n, arr1, arr2):
#     answer = []

#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n, '0')
#         a12=a12.replace('1', '#')
#         a12=a12.replace('0', ' ')
#         answer.append(a12)

#     return answer


# solution = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])
