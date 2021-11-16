def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[len(phone_number) - 4:]

# def solution(s):
#     return "*" * (len(s) - 4) + s[-4:]