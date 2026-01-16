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
    ((2, 29, 2004, 2, 28, 2009), (1827, 2, 522, 1305, 3, 3, 4, 3, 13, 1292)),
    ((2, 29, 2008, 7, 19, 2008), (142, 1, 41, 101, 0, 1, 0, 0, 1, 100)),
    ((2, 28, 1989, 2, 29, 1996), (2558, 2, 730, 1828, 5, 5, 6, 5, 21, 1807)),
    ((5, 30, 1992, 2, 29, 2004), (4293, 3, 1228, 3065, 9, 8, 8, 9, 34, 3031)),
    ((6, 3, 1996, 10, 23, 1996), (143, 0, 40, 103, 0, 0, 0, 0, 0, 103)),
    ((1, 23, 2000, 7, 26, 2000), (186, 1, 53, 133, 0, 1, 0, 0, 1, 132)),
    ((5, 7, 1988, 12, 19, 1992), (1688, 1, 483, 1205, 3, 4, 4, 3, 14, 1191)),
    ((12, 29, 1980, 12, 31, 1980), (3, 0, 0, 3, 0, 0, 0, 0, 0, 3))
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
        labels = [
            "total days from start date to end date",
            "total additional days from leap years",
            "total weekends",
            "total days without weekends",
            "new year holiday",
            "labor day holiday",
            "all saints day holiday",
            "christmas holiday",
            "total holidays",
            "total working days"
        ]

        # Table header
        print(f"{'Metric':40} {'Output':8} {'Expected':10} Status")
        print("-" * 70)

        # Compare results
        all_passed = True

        for i in range(len(labels)):
            output = result[i]
            expected_val = expected[i]
            if output == expected_val:
                status = "✓"
            else:
                status = "✗"
                all_passed = False

            print(f"{labels[i]:40} {output:<8} {expected_val:<10} {status}")

        # Final result
        print("-" * 70)
        
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

    print("-" * 70)
    
    
