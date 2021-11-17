def solution(s):
    arr = list(map(int, s.split(' ')))
    return '{} {}'.format(min(arr), max(arr))