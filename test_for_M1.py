from Milestone_1 import (
    compute_total_days, 
    compute_weekdays, 
    compute_leap_days)

# Test cases: each tuple is (inputs, expected_outputs)
# inputs: (start_month, start_day, start_year, end_month, end_day, end_year)
# expected_outputs: (total_days, leap_days, weekends, weekdays)
test_cases = [
    ((4, 28, 1983, 2, 24, 1996), (4686, 3, 1339, 3347)),
    ((12, 29, 2005, 6, 13, 2010), (1628, 1, 466, 1162)),
    ((3, 19, 1971, 10, 3, 1986), (5678, 4, 1622, 4056)),
    ((7, 7, 1977, 7, 7, 1978), (366, 0, 104, 262)),
    ((2, 29, 2004, 2, 28, 2009), (1827, 2, 522, 1305)),
    ((2, 29, 2008, 7, 19, 2008), (142, 1, 41, 101)),
    ((2, 28, 1989, 2, 29, 1996), (2558, 2, 730, 1828)),
    ((5, 30, 1992, 2, 29, 2004), (4293, 3, 1228, 3065)),
    ((6, 3, 1996, 10, 23, 1996), (143, 0, 40, 103)),
    ((1, 23, 2000, 7, 26, 2000), (186, 1, 53, 133)),
    ((5, 7, 1988, 12, 19, 1992), (1688, 1, 483, 1205)),
    ((12, 29, 1980, 12, 31, 1980), (3, 0, 0, 3)),
    ((6, 18, 1985, 2, 28, 1988), (986, 0, 282, 704)),
    ((1, 23, 2012, 2, 21, 2012), (30, 0, 8, 22))
]

for i, (inputs, expected) in enumerate(test_cases):

    # Compute outputs using your functions
    total_days = compute_total_days(*inputs)
    weekdays = compute_weekdays(*inputs)
    weekends = total_days - weekdays
    leap_days = compute_leap_days(*inputs)
   
    result = (
        total_days,
        leap_days,
        weekends,
        weekdays
    )

    print(f"Test Case {i}")
    print(f"Inputs: {inputs}")
    print(f"total days from start date to end date: {result[0]}")
    print(f"Correct Answer : {expected[0]}")
    print(f"total additional days from leap years: {result[1]}")
    print(f"Correct Answer : {expected[1]}")
    print(f"total weekends: {result[2]}") 
    print(f"Correct Answer : {expected[2]}")
    print(f"total days without weekends: {result[3]}")
    print(f"Correct Answer : {expected[3]}")

    #Check if outputs match expected
    if (result) == expected:
        print("Result: ✅ PASS")
    else:
        print("Result: ❌ FAIL")
    print("-" * 50)