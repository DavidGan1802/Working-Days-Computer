from Milestone_1 import compute_total_days, compute_weekdays, compute_leap_days

# Test cases: each tuple is (inputs, expected_outputs)
# inputs: (start_month, start_day, start_year, end_month, end_day, end_year)
# expected_outputs: (total_days, leap_days, weekends, weekdays)
test_cases = [
    ((4, 28, 1983, 2, 24, 1996), (4686, 3, 1339, 3347)),
    ((12, 29, 2005, 6, 13, 2010), (1628, 1, 466, 1162)),
    ((3, 19, 1971, 10, 3, 1986), (5678, 4, 1622, 4056)),
    ((7, 7, 1977, 7, 7, 1978), (366, 0, 104, 262))
]

for i, (inputs, expected) in enumerate(test_cases):

    # Compute outputs using your functions
    total_days = compute_total_days(*inputs)
    weekdays = compute_weekdays(*inputs)
    weekends = total_days - weekdays
    leap_days = compute_leap_days(*inputs)

    # Print in the same format as the original program
    print ("Enter start month: Enter start day: Enter start year: Enter end month: Enter end day: Enter end year:")    
    print(f"total days from start date to end date: {total_days}")
    print(f"\ntotal additional days from leap years: {leap_days}")
    print(f"\ntotal weekends: {weekends}") 
    print(f"\ntotal days without weekends: {weekdays}")

    #Check if outputs match expected
    if (total_days, leap_days, weekends, weekdays) == expected:
        print("Result: ✅ PASS")
    else:
        print("Result: ❌ FAIL")
    print("-" * 100)