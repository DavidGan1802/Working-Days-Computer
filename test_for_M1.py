from Milestone_1 import (
    compute_total_days,
    compute_weekdays,
    compute_leap_days
)

test_cases = [
    # (start_month, start_day, start_year, end_month, end_day, end_year)
    (4, 28, 1983, 2, 24, 1996),
    (12, 29, 2005, 6, 13, 2010),
]

for case in test_cases:
    total_days = compute_total_days(*case)
    weekdays = compute_weekdays(*case)
    weekends = total_days - weekdays
    leap_days = compute_leap_days(*case)

    print("Input:", case)
    print("Total days:", total_days)
    print("Leap days:", leap_days)
    print("Weekends:", weekends)
    print("Weekdays:", weekdays)
    print("-" * 40)