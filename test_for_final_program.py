from Final_Program import (
    error_checker_date,
    compute_total_days,
    compute_weekdays,
    compute_leap_days,
    compute_holidays
)

test_cases = [
    
    ((4, 28, 1983, 2, 24, 1996), (4686, 3, 1339, 3347, 9, 9, 10, 9, 37, 3310)),
    ((12, 29, 2005, 6, 13, 2010), (1628, 1, 466, 1162, 4, 4, 2, 4, 14, 1148)),
    ((3, 19, 1971, 10, 3, 1986), (5678, 4, 1622, 4056, 10, 11, 12, 10, 43, 4013)),
    ((7, 7, 1977, 7, 7, 1978), (366, 0, 104, 262, 0, 1, 1, 0, 2, 260)),
    ((1, 1, 1971, 12, 31, 3030), "Invalid Input. Exiting Program."),
    ((1, 33, 1971, 12, 31, 2020), "Invalid Input. Exiting Program."),
    (("a", 1, 1971, 12, 31, 2020), "Invalid Input. Exiting Program."),
]

for i, (inputs, expected) in enumerate(test_cases):

    print(f"Test Case {i}")
    print(f"Inputs: {inputs}")
    
    try:
        start_month, start_day, start_year, end_month, end_day, end_year = inputs

        # Validate dates
        error_checker_date(start_month, start_day, start_year)
        error_checker_date(end_month, end_day, end_year)

        total_days = compute_total_days(*inputs)
        weekdays = compute_weekdays(*inputs)
        weekends = total_days - weekdays
        leap_days = compute_leap_days(*inputs)
        holidays = compute_holidays(*inputs)
        total_holidays = holidays[4]
        workdays = total_days - weekends - total_holidays

        result = (
            total_days,
            leap_days,
            weekends,
            weekdays,
            holidays[0],
            holidays[1],
            holidays[2],
            holidays[3],
            total_holidays,
            workdays
        )

        print(f"total days from start date to end date: {result[0]}")
        print(f"Correct Answer : {expected[0]}")
        print(f"total additional days from leap years: {result[1]}")
        print(f"Correct Answer : {expected[1]}")
        print(f"total weekends: {result[2]}") 
        print(f"Correct Answer : {expected[2]}")
        print(f"total days without weekends: {result[3]}")
        print(f"Correct Answer : {expected[3]}")
        print(f"new year holiday: {result[4]}")
        print(f"Correct Answer : {expected[4]}")
        print(f"labor day holiday: {result[5]}")
        print(f"Correct Answer : {expected[5]}")
        print(f"all saints day holiday: {result[6]}")
        print(f"Correct Answer : {expected[6]}")
        print(f"christmas holiday: {result[7]}")
        print(f"Correct Answer : {expected[7]}")        
        print(f"total holidays: {result[8]}")
        print(f"Correct Answer : {expected[8]}")
        print(f"total working days: {result[9]}")
        print(f"Correct Answer : {expected[9]}")
        
        if result == expected:
            print("Result: ✅ PASS")
        else:
            print("Result: ❌ FAIL")

    except SystemExit:
        print(f"Correct Answer : {expected}")

        if expected == "Invalid Input. Exiting Program.":
            print("Result: ✅ PASS")
        else:
            print("Result: ❌ FAIL")

    print("-" * 50)
    
    
