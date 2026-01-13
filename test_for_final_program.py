from Final_Program import (
    error_checker_date,
    compute_total_days,
    compute_weekdays,
    compute_leap_days,
    compute_holidays
)

test_cases = [
    # Valid cases
    ((4, 28, 1983, 2, 24, 1996), (4686, 3, 1339, 3347, 9, 10, 9, 37, 3310)),
    ((12, 29, 2005, 6, 13, 2010), (1628, 1, 466, 1162, 4, 4, 2, 4, 14, 1148)),
    ((3, 19, 1971, 10, 3, 1986), (5678, 4, 1622, 4056, 10, 11, 12, 10, 43, 4013)),
    ((7, 7, 1977, 7, 7, 1978), (366, 0, 104, 262, 0, 1, 1, 0, 2, 260)),

    # Invalid cases
    ((1, 1, 1971, 12, 31, 3030), "Invalid Input"),
    ((1, 33, 1971, 12, 31, 2020), "Invalid Input"),
    (("a", 1, 1971, 12, 31, 2020), "Invalid Input"),
]

for i, (inputs, expected) in enumerate(test_cases, start=1):

    print(f"\nTest Case {i}")
    print(f"Inputs: {inputs}")

    try:
        sm, sd, sy, em, ed, ey = inputs

        # Validate dates
        error_checker_date(sm, sd, sy)
        error_checker_date(em, ed, ey)

        total_days = compute_total_days(sm, sd, sy, em, ed, ey)
        weekdays = compute_weekdays(sm, sd, sy, em, ed, ey)
        weekends = total_days - weekdays
        leap_days = compute_leap_days(sm, sd, sy, em, ed, ey)

        holidays = compute_holidays(sm, sd, sy, em, ed, ey)
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

        print(f"Computed Output : {result}")
        print(f"Expected Output : {expected}")

        if result == expected:
            print("Result: ✅ PASS")
        else:
            print("Result: ❌ FAIL")

    except SystemExit:
        print("Program exited due to invalid input.")
        print(f"Expected Output : {expected}")

        if expected == "Invalid Input":
            print("Result: ✅ PASS")
        else:
            print("Result: ❌ FAIL")

    print("-" * 60)
