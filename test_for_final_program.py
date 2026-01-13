from Final_Program import get_int_input, error_checker_date, compute_total_days, compute_weekdays, compute_leap_days, compute_holidays

# Test cases: each tuple is (inputs, expected_outputs)
# inputs: (start_month, start_day, start_year, end_month, end_day, end_year)
# expected_outputs: (total_days, leap_days, weekends, weekdays)
test_cases = [
    ((4, 28, 1983, 2, 24, 1996), (4686, 3, 1339, 3347, 9, 10, 9, 37, 3310)),
    ((12, 29, 2005, 6, 13, 2010), (1628, 1, 466, 1162, 4, 4, 2, 4, 14, 1148)),
    ((3, 19, 1971, 10, 3, 1986), (5678, 4, 1622, 4056, 10, 11, 12, 10, 43, 4013)),
    ((7, 7, 1977, 7, 7, 1978), (366, 0, 104, 262, 0, 1, 1, 0, 2, 260)),
    ((1, 1, 1971, 12, 31, 3030), ("Invalid Input")),
    ((1, 33, 1971, 12, 31, 2020), ("Invalid Input")),
    (("a", 1, 1971, 12, 31, 2020), ("Invalid Input"))
]

for i, (inputs, expected) in enumerate(test_cases):

    # Compute outputs using your functions
    total_days = compute_total_days(*inputs)
    weekdays = compute_weekdays(*inputs)
    weekends = total_days - weekdays
    leap_days = compute_leap_days(*inputs)
   
    print(f"Test Case {i}")
    print(f"total days from start date to end date: {total_days}")
    print(f"Correct Answer : {expected[0]}")
    print(f"total additional days from leap years: {leap_days}")
    print(f"Correct Answer : {expected[1]}")
    print(f"total weekends: {weekends}") 
    print(f"Correct Answer : {expected[2]}")
    print(f"total days without weekends: {weekdays}")
    print(f"Correct Answer : {expected[3]}")

    #Check if outputs match expected
    if (total_days, leap_days, weekends, weekdays) == expected:
        print("Result: ✅ PASS")
    else:
        print("Result: ❌ FAIL")
    print("-" * 50)