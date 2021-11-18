def solution(a, b):
    answer = ''
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    
    answer = day[(sum(mon[:a - 1]) + b) % 7]
    
    return answer

# import datetime

# def solution(a, b): 
#     day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
#     return day[datetime.datetime(year=2016, month=a, day=b).weekday()]