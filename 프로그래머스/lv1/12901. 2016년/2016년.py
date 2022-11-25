import calendar
def solution(a, b):
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    return day[calendar.weekday(2016,a,b)]