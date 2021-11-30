def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        # q를 base로 변환
        # 즉, n진수의 다음 자리를 구함
        return convert(q, base) + temp[r]
    
def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m*t):
        test += str(convert(i, n))
        
    while len(answer) < t:
        answer += test[p - 1]
        p += m
        
    return answer

big = ["A","B","C","D","E","F"]

def solution(n, t, m, p):
    a = "0"
    i = 0
    #for i in range(t*m):
    while True:
        if len(a) >= t * m:
            break
        b = ""
        j = i
        while (j):
            if j % n > 9:
                b = big[j % n - 10] + b
            else:
                b = str(j % n) + b
            j = j // n
        a = a + b
        i = i + 1
    answer = a[p - 1 :: m][:t]
    return answer