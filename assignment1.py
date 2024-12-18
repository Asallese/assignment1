#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: "Asallese2"
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        raise ValueError('Invalid Month')
# With this definition, the first if in the loop only have 31 days, second statement has months with 30days, and the final is february and will return if defined leap_year is else then 28. For error handling i used ValueError if month is not between 1 to 12.
    "returns the maximum day for a given month. Includes leap year check"
    ...
def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format
# after() is used to schedule a function call after a given delay.

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date

def usage()
    print("Usage. assignment1.py <arg1> <arg2>")
    sys.exit(1)
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
# in the above function, i made my definiton work by the following. If said year is divisible by 4, 100 , and 400 it is a leap year. If it is divisible by 4 and 100 but not by 400, it is not a leap year.If it is divisible by 4 but not by 100 it is a leap year. Finally if it is not divisible by 4 it is not a leap year.
"return True if the year is a leap year"
    ...

def valid_date(date: str) -> bool:

    #"check validity of date and return True if valid"
    try:
        year, month, day = [int(x) for x in date.split('-')]
    except ValueError:
        print('Error, Invalid Date')
        return False

    if year < 1500:
        return False
    else:
        if month < 1 or month > 12:
            return False

# I then made an else   statement to confirm whether the day is greater than one and less then the mon_max which is defined above and will parse the data and confirm whether or not the month and the year are within the max. If so, it will return as true.

    ...

def day_count(start_date: str, stop_date: str) -> int:
    weekends = 0
    daycount_date = start_date

    while daycount_date <= stop_date:
        str_year, str_month, str_day = daycount_date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        name_day = day_of_week(year, month, day)

        if name_day == 'sat' or name_day == 'sun':
            weekends += 1

        daycount_date = after(daycount_date)

    return weekends
    "Loops through range of dates, and returns number of weekend days"
    ...
# For day_count, i start by making weekends = 0 and will be keeping track of the weekends. I then made daycount_date as start date to be iterated through each date. As long as it is less then or equal to teh date, the while loop will countinue.

# I used day of the week function to showthe list of days made above and be put into a if statement. with name_day being day of week, i made it == to either sat or sun and it will incrase the counter. Based on however many weeknds it will use after().

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        usage('Usage. assignment1.py <arg1> <arg2>')

    start_date, end_date = sys.argv[1], sys.argv[2]


    if not valid_date(start_date) or not valid_date(end_date):
        print("start_date or end_date or both given dates are invalid.")
        usage()

    if start_date > end_date:
        print("Start date appears to earlier then the end date! Swapping..")
        start_date, end_date = end_date, start_date

    weekends = day_count(start_date, end_date)

    print("The number of weekend days between " + start_date + " and " + end_date + " is: " + str(weekends))
    ...

