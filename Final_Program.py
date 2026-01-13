import calendar
import datetime
import sys

#References : https://docs.python.org/2/library/datetime.html
#References : https://docs.python.org/2/library/calendar.html
#References : https://docs.python.org/3/tutorial/errors.html
#References : https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/

def error_checker(month, day, year):
    
    if not (1 <= month <= 12):
        print("\nInvalid Input. Exiting Program.")
        sys.exit()     
    
    if month == 2:
        max_day = 29 if calendar.isleap(year) else 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31
    if not (1 <= day <= max_day):
        print("\nInvalid Input. Exiting Program.")
        sys.exit()
    
    if not (1971 <= year <= 2020):
        print("\nInvalid Input. Exiting Program.")
        sys.exit()
    
    return True

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

def compute_holidays(start_month, start_day, start_year, end_month, end_day, end_year):
    
    start = datetime.date(start_year, start_month, start_day)
    end = datetime.date(end_year, end_month, end_day)
    total = end - start
    total_days = total.days + 1 
    
    new_year = 0
    labor_day = 0
    all_saints_day = 0
    christmas = 0

    for i in range(total_days):
        current = start + datetime.timedelta(days=i)

        if current.weekday() < 5:
            if current.month == 1 and current.day == 1:
                new_year += 1
            elif current.month == 5 and current.day == 1:
                labor_day += 1
            elif current.month == 11 and current.day == 1:
                all_saints_day += 1
            elif current.month == 12 and current.day == 25:
                christmas += 1
            
    total = new_year + labor_day + all_saints_day + christmas

    return new_year, labor_day, all_saints_day, christmas, total


if __name__ == '__main__':

    start_month = int(input("Enter start month: ").strip())
    start_day   = int(input("Enter start day: ").strip())
    start_year  = int(input("Enter start year: ").strip())

    end_month   = int(input("Enter end month: ").strip())
    end_day     = int(input("Enter end day: ").strip())
    end_year    = int(input("Enter end year: ").strip())
    
    error_checker(start_month, start_day, start_year)
    error_checker(end_month, end_day, end_year)

    total_days = compute_total_days(start_month, start_day, start_year, end_month, end_day, end_year)
    weekdays = compute_weekdays(start_month, start_day, start_year, end_month, end_day, end_year)
    weekends = total_days - weekdays
    leap_days = compute_leap_days(start_month, start_day, start_year, end_month, end_day, end_year)
    holidays = compute_holidays(start_month, start_day, start_year, end_month, end_day, end_year)
    workdays = total_days - weekends - holidays[4]
       
    print(f"\ntotal days from start date to end date: {total_days}")
    print(f"\ntotal additional days from leap years: {leap_days}")
    print(f"\ntotal weekends: {weekends}") 
    print(f"\ntotal days without weekends: {weekdays}")
    print(f"\nnew year holiday: {holidays[0]}")
    print(f"labor day holiday: {holidays[1]}")
    print(f"all saints day holiday: {holidays[2]}")
    print(f"christmas holiday: {holidays[3]}")
    print(f"total holidays: {holidays[4]}")
    print(f"\ntotal working days: {workdays}")