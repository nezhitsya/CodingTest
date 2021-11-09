import math

def solution(w,h):
    answer = w * h - (w + h - math.gcd(w, h)) # gcd : 최대공약수
    return answer

# def gcd(a,b): 
#     return b if (a == 0) else gcd(b % a,a)

# def solution(w,h):
#     return w * h - w - h + gcd(w,h)
