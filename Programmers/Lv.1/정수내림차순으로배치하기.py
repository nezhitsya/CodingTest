def solution(n):
    n_list = list(str(n))
    n_list.sort(reverse = True)
    return int(''.join(n_list))

# def solution(n):
#     return int("".join(sorted(str(n), reverse=True)))