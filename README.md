# My Software Project for EEE 111 (Introduction to Programming Computation)

This software project computes the number of working days for a given time frame using the Gregorian calendar.
The project is heavily inspired by the website: http://hungary.workingdays.org/

The program computes the total number of working days between two given dates, defined as a weekday
disregarding both holidays landing on a weekday and weekends (Saturday and Sunday).

## The code includes the following functions:

- compute_total_days(): Computes the total number of days from the start date to end date
- compute_weekdays(): Computes the total number of weekends from the start date to end date
- compute_leap_years(): Computes the number of extra days from leap years between the start date to end date
- compute_holidays(): Computes the number of New Year days, Labor days, All Saints' day, Christmas days between the start date to end date (holidays landing on a weekend are not considered)
- compute_workdays(): Computes the total number of workdays, defined as weekdays disregarding both the weekends and holidays landing on a weekday.

## Inputs:
- Day of start date (integer)
- Month of start date (integer)
- Year of start date (integer)
- Day of end date - inclusive (integer)
- Month of end date (integer)
- Year of end date (integer)

## Outputs:
1) Number of days between the start day to end day, inclusive of the end date. (integer)
2) Number of weekdays and weekends between the start day to end day, inclusive of the end date. (integer)
3) Number of extra days from leap years. (integer)
4) Total number of holidays, including the total number of each holiday (integer)
5) Number of working days between the start date and end date, inclusive of the end date. (integer)

## Error Checking:
1) The input dates should be within the date limit (January 1, 1971 to December 31, 2020).
2) The input dates should be valid (January has 31 days, December has 31 days, etc.).
3) All inputs should be an integer.

Credits: UPD EEE 111 Professors

References: http://hungary.workingdays.org/
