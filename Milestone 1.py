import calendar
import datetime


#References : https://docs.python.org/2/library/datetime.html
#References : https://docs.python.org/2/library/calendar.html

def compute_total_days(start_month, start_day, start_year, end_month, end_day, end_year):
    
    #datetime.date turns a calendar date into a type that can support mathematical and relational operations.
    start = datetime.date(start_year, start_month, start_day)
    end = datetime.date(end_year, end_month, end_day)
    total = end - start
    total_days = total.days + 1
        
    return total_days

def compute_weekdays(start_month, start_day, start_year, end_month, end_day, end_year):
    
    start = datetime.date(start_year, start_month, start_day)
    end = datetime.date(end_year, end_month, end_day)  
    total = end - start
    total_days = total.days + 1
    full_weeks = total_days // 7
    weekdays = full_weeks * 5
    
    #datetime.timedelta represents a duration of time. It can be days, hours, minutes etc.
    #the .weekday() function generates a int 0-6 wherein 0 represents Monday, 1 represents Tuesday and so on
    #until Sunday which equals to 6.
    remaining_days = total_days % 7 
    for i in range(remaining_days):
        if (start + datetime.timedelta(days=full_weeks * 7 + i)).weekday() < 5:
            weekdays += 1
            
    return weekdays

def compute_leap_days(start_month, start_day, start_year, end_month, end_day, end_year):
    
    start = datetime.date(start_year, start_month, start_day)
    end = datetime.date(end_year, end_month, end_day)
    
    leap_days = 0
    for year in range(start_year, end_year + 1):
        if calendar.isleap(year):
            if start <= datetime.date(year, 2, 29) <= end:
                leap_days += 1
    
    return leap_days
    
if __name__ == '__main__':
    start_month = int(input().strip())

    start_day = int(input().strip())

    start_year = int(input().strip())
    
    end_month = int(input().strip())

    end_day = int(input().strip())

    end_year = int(input().strip())

    total_days = compute_total_days(start_month, start_day, start_year, end_month, end_day, end_year)
    weekdays = compute_weekdays(start_month, start_day, start_year, end_month, end_day, end_year)
    weekends = total_days - weekdays
    leap_days = compute_leap_days(start_month, start_day, start_year, end_month, end_day, end_year)
    
    print ("Enter start month: Enter start day: Enter start year: Enter end month: Enter end day: Enter end year:")    
    print(f"total days from start date to end date: {total_days}")
    print(f"\ntotal additional days from leap years: {leap_days}")
    print(f"\ntotal weekends: {weekends}") 
    print(f"\ntotal days without weekends: {weekdays}")