def solution(n):
    answer = ''

    while n > 0:			
        n, re = divmod(n, 3)	# n을 3으로 나눈 몫과 나머지
        answer += str(re)
        
    return int(answer, 3)

# int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌

