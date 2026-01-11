from Milestone_1 import compute_total_days, compute_weekdays, compute_leap_days

# Test cases: each tuple is (inputs, expected_outputs)
# inputs: (start_month, start_day, start_year, end_month, end_day, end_year)
# expected_outputs: (total_days, leap_days, weekends, weekdays)
test_cases = [
    ((4, 28, 1983, 2, 24, 1996), (4743, 4, 1351, 3392)),
    ((12, 29, 2005, 6, 13, 2010), (1621, 1, 463, 1158)),
]

for i, (inputs, expected) in enumerate(test_cases, 1):
    total_days = compute_total_days(*inputs)
    weekdays = compute_weekdays(*inputs)
    weekends = total_days - weekdays
    leap_days = compute_leap_days(*inputs)

    actual = (total_days, leap_days, weekends, weekdays)
    print(f"Test case {i}: inputs = {inputs}")
    print(f"Expected: {expected}")
    print(f"Actual  : {actual}")

    if actual == expected:
        print("Result: ✅ PASS")
    else:
        print("Result: ❌ FAIL")
    print("-" * 40)
