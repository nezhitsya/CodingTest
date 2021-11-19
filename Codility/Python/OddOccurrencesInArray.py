def solution(A):
    A_dict = dict()

    # A 요소를 key로, 만약 이미 값이 존재하면 삭제, 그렇지 않으면 boolean 값 부여
    for i in A:
        try:
            del A_dict[i]
        except:
            A_dict[i] = True
    
    # boolean 값을 보유하면 키값 리턴
    for key, val in A_dict.items():
        if val:
            return key

print(solution([9, 3, 9, 3, 9, 7, 9])) # 7