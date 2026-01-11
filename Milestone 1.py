import calendar
import datetime


#References : https://docs.python.org/2/library/datetime.html
#References : https://docs.python.org/2/library/calendar.html

def compute_total_days(s_m, s_d, s_y, e_m, e_d, e_y):
    start  = datetime.date(s_y, s_m, s_d)
    end = datetime.date(e_y, e_m, e_d)
    total = end - start
    return total.days + 1

def compute_weekdays(s_m, s_d, s_y, e_m, e_d, e_y):
    start  = datetime.date(s_y, s_m, s_d)
    end = datetime.date(e_y, e_m, e_d)
    total = (end - start).days
    day_of_start = start.weekday()
    day_of_end = end.weekday()
    if day_of_start == 0 and day_of_end == 0: 
        return int((total//7) * 2)
    elif day_of_start == 0 and day_of_end == 1: 
        return int((total//7) * 2)
    elif day_of_start == 0 and day_of_end == 2: 
        return int((total//7) * 2)
    elif day_of_start == 0 and day_of_end == 3: 
        return int((total//7) * 2)
    elif day_of_start == 0 and day_of_end == 4: 
        return int((total//7) * 2)
    elif day_of_start == 0 and day_of_end == 5: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 0 and day_of_end == 6: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 1 and day_of_end == 0: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 1 and day_of_end == 1: 
        return int((total//7) * 2)
    elif day_of_start == 1 and day_of_end == 2: 
        return int((total//7) * 2)
    elif day_of_start == 1 and day_of_end == 3: 
        return int((total//7) * 2)
    elif day_of_start == 1 and day_of_end == 4: 
        return int((total//7) * 2)
    elif day_of_start == 1 and day_of_end == 5: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 1 and day_of_end == 6: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 2 and day_of_end == 0: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 2 and day_of_end == 1: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 2 and day_of_end == 2: 
        return int((total//7) * 2)
    elif day_of_start == 2 and day_of_end == 3: 
        return int((total//7) * 2)
    elif day_of_start == 2 and day_of_end == 4: 
        return int((total//7) * 2)
    elif day_of_start == 2 and day_of_end == 5: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 2 and day_of_end == 6: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 3 and day_of_end == 0: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 3 and day_of_end == 1: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 3 and day_of_end == 2: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 3 and day_of_end == 3: 
        return int((total//7) * 2)
    elif day_of_start == 3 and day_of_end == 4: 
        return int((total//7) * 2)
    elif day_of_start == 3 and day_of_end == 5: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 3 and day_of_end == 6: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 4 and day_of_end == 0: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 4 and day_of_end == 1: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 4 and day_of_end == 2: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 4 and day_of_end == 3: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 4 and day_of_end == 4: 
        return int((total//7) * 2)
    elif day_of_start == 4 and day_of_end == 5: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 4 and day_of_end == 6: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 5 and day_of_end == 0: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 5 and day_of_end == 1: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 5 and day_of_end == 2: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 5 and day_of_end == 3: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 5 and day_of_end == 4: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 5 and day_of_end == 5: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 5 and day_of_end == 6: 
        return int(((total//7) * 2) + 2)
    elif day_of_start == 6 and day_of_end == 0: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 6 and day_of_end == 1: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 6 and day_of_end == 2: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 6 and day_of_end == 3: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 6 and day_of_end == 4: 
        return int(((total//7) * 2) + 1)
    elif day_of_start == 6 and day_of_end == 5: 
        return int(((total//7) * 2) + 2)
    else: 
        return int(((total//7) * 2) + 2)

def compute_leap_years(s_y, e_y):
    start1  = datetime.datetime(s_y, s_m, s_d)
    end1 = datetime.datetime(e_y, e_m, e_d)
    if calendar.isleap(s_y) == True and calendar.isleap(e_y) == True:
        if start1 >= datetime.datetime(s_y, 3, 1):
            if end1 <= datetime.datetime(e_y, 2, 28):
                return calendar.leapdays(s_y+1,e_y)
            else: 
                return calendar.leapdays(s_y+1,e_y) + 1
        else:
            if end1 <= datetime.datetime(e_y, 2, 28):
                return calendar.leapdays(s_y+1,e_y) + 1
            else:
                return calendar.leapdays(s_y+1,e_y) + 2
    elif calendar.isleap(s_y) == False and calendar.isleap(e_y) == False :
        return calendar.leapdays(s_y,e_y) 
    elif calendar.isleap(s_y) == True and calendar.isleap(e_y) == False :
        if start1 >= datetime.datetime(s_y, 3, 1):
            return calendar.leapdays(s_y + 1,e_y)
        else:
            return calendar.leapdays(s_y + 1,e_y) + 1
    elif calendar.isleap(s_y) == False and calendar.isleap(e_y) == True:
        if end1 <= datetime.datetime(e_y, 2, 28):
            return calendar.leapdays(s_y,e_y) 
        else:
            return calendar.leapdays(s_y,e_y) + 1
if __name__ == '__main__':
    s_m = int(input().strip())

    s_d = int(input().strip())

    s_y = int(input().strip())
    
    e_m = int(input().strip())

    e_d = int(input().strip())

    e_y = int(input().strip())
 
print ("Enter start month: Enter start day: Enter start year: Enter end month: Enter end day: Enter end year:")    
print ("total days from start date to end date:" , compute_total_days(s_m, s_d, s_y, e_m, e_d, e_y))
print("")
print ("total additional days from leap years:", compute_leap_years(s_y,e_y) )
print("")
print ('total weekends:', compute_weekdays(s_m, s_d, s_y, e_m, e_d, e_y) )
print("")
print ("total days without weekends:", (compute_total_days(s_m, s_d, s_y, e_m, e_d, e_y) - compute_weekdays(s_m, s_d, s_y, e_m, e_d, e_y)))